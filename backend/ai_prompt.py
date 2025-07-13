# ai_prompt.py

RISK_REPORT_SCHEMA = """
{
  "project": {
    "name": "string",
    "organization": "string",
    "description": "string",
    "goals": ["string"],
    "deliverables": ["string"]
  },
  "risks": [
    {
      "title": "string",
      "description": "string",
      "severity": "very_high|high|medium|low",
      "impacts": ["string"],
      "opportunities": ["string"],
      "metrics": {
        "probability": "1-5",
        "impact": "1-5",
        "overall": "1-5"
      },
      "strategy": "string"
    }
  ],
  "innovation": {
    "score": "1-10",
    "components": [
      {"title": "string", "score": "1-10"}
    ]
  },
  "regulation": {
    "table": [
      {"requirement": "string", "status": "string"}
    ]
  },
  "summary": "string",
  "recommendations": ["string"]
}
"""

PROMPT_TEMPLATE = f"""
אתה מנתח סיכונים חכם. קבל את תוכן המסמך, נתח אותו, והחזר אך ורק JSON תקני לפי הסכמה הבאה:
{RISK_REPORT_SCHEMA}
"""
