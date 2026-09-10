SEVERITIES={"sev1":15,"sev2":30,"sev3":120}

def acknowledgement_ok(severity,minutes):
    return minutes<=SEVERITIES[severity]

def incident_summary(incident_id,severity,minutes_to_ack,minutes_to_restore):
    return {
        "incident_id":incident_id,
        "severity":severity,
        "ack_sla_met":acknowledgement_ok(severity,minutes_to_ack),
        "minutes_to_restore":minutes_to_restore,
    }
