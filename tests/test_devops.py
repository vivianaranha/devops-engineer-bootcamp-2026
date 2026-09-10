import sys,tempfile,unittest
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))

from devops_engineering.release import sha256,release_allowed
from devops_engineering.semver import parse,bump
from devops_engineering.slo import availability,error_budget,budget_remaining
from devops_engineering.deployment import rollout_decision,canary_split
from devops_engineering.k8s import resource_findings,probe_review
from devops_engineering.iac import validate_plan
from devops_engineering.incident import acknowledgement_ok,incident_summary
from devops_engineering.security import pipeline_security_review
from devops_engineering.platform import golden_path_score

class DevOpsTests(unittest.TestCase):
    def test_release(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"a";p.write_text("x")
            self.assertEqual(len(sha256(p)),64)
        self.assertTrue(release_allowed({"tests":True,"scan":True})["allowed"])
        self.assertFalse(release_allowed({"tests":False})["allowed"])
    def test_semver(self):
        self.assertEqual(parse("v1.2.3"),(1,2,3))
        self.assertEqual(bump("1.2.3","patch"),"1.2.4")
        self.assertEqual(bump("1.2.3","minor"),"1.3.0")
    def test_slo(self):
        self.assertEqual(availability(99,100),.99)
        self.assertAlmostEqual(error_budget(100000,.999),100)
        self.assertLess(budget_remaining(100000,120,.999)["remaining"],0)
    def test_deployment(self):
        self.assertTrue(rollout_decision(.005,200,.01,250)["continue"])
        self.assertFalse(rollout_decision(.02,200,.01,250)["continue"])
        self.assertEqual(canary_split(100,10),{"canary":10,"stable":90})
    def test_k8s(self):
        self.assertEqual(resource_findings("100m","500m","128Mi","512Mi"),[])
        self.assertTrue(probe_review("/ready","/health")["production_ready"])
        self.assertFalse(probe_review("", "/health")["production_ready"])
    def test_iac(self):
        plan=[{"resource":"db","action":"delete","approved":False,"tags":{"owner":"x"}}]
        findings=validate_plan(plan)
        self.assertTrue(any(x["issue"]=="unapproved_delete" for x in findings))
        self.assertTrue(any(x["issue"]=="missing_tags" for x in findings))
    def test_incident(self):
        self.assertTrue(acknowledgement_ok("sev1",10))
        self.assertFalse(acknowledgement_ok("sev1",20))
        self.assertEqual(incident_summary("i","sev2",20,50)["severity"],"sev2")
    def test_security(self):
        cfg={"token_permissions":"write-all","secrets_in_repo":True,"dependency_scan":False,"artifact_checksum":False}
        self.assertEqual(len(pipeline_security_review(cfg)),4)
    def test_platform(self):
        r=golden_path_score(["repo_template","ci","deployment"])
        self.assertLess(r["score"],1)
        self.assertIn("rollback",r["missing"])

if __name__=="__main__": unittest.main()
