#!/usr/bin/env python3
"""
Psychometric Career Intelligence
An educational resource that explores the science of psychometric assessments
and career decision making — helping students discover their strengths,
identify suitable career paths, and make informed academic and professional
decisions through evidence based insights.
https://psychometric.fyi
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "personality_trait": "Personality Trait",
        "cognitive_ability": "Cognitive Ability",
        "interest_alignment": "Interest Alignment",
        "motivation_clarity": "Motivation Clarity",
        "strength_discovery": "Strength Discovery",
        "career_readiness": "Career Readiness",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_recommended_pathways(interest: int, cognitive: int, personality: int) -> dict:
    return {
        "STEM & Technology": min(100, round(cognitive * 1.05)),
        "Creative & Design": min(100, round(personality * 0.95)),
        "Business & Leadership": min(100, round(interest * 1.0)),
        "Social & Education": min(100, round((personality + interest) / 2)),
    }


def analyze_career_intelligence(
    profile: str,
    assessment_type: str = "personality",
    personality_trait: int = 82,
    cognitive_ability: int = 78,
    interest_alignment: int = 85,
    motivation_clarity: int = 74,
    strength_discovery: int = 88,
    career_readiness: int = 76,
) -> dict:
    """
    Analyze psychometric assessment signals for career intelligence.

    Args:
        profile: Student or individual profile identifier
        assessment_type: Type of psychometric assessment
        personality_trait: Personality trait score (0-100)
        cognitive_ability: Cognitive ability score (0-100)
        interest_alignment: Interest alignment score (0-100)
        motivation_clarity: Motivation clarity score (0-100)
        strength_discovery: Strength discovery score (0-100)
        career_readiness: Career readiness score (0-100)

    Returns:
        dict with individual signal scores, overall career intelligence,
        and recommended career pathways
    """
    scores = {
        "personality_trait": personality_trait,
        "cognitive_ability": cognitive_ability,
        "interest_alignment": interest_alignment,
        "motivation_clarity": motivation_clarity,
        "strength_discovery": strength_discovery,
        "career_readiness": career_readiness,
    }
    overall_career_intelligence = round(sum(scores.values()) / 6)

    return {
        "profile": profile,
        "assessment_type": assessment_type.capitalize(),
        "personality_trait_score": personality_trait,
        "cognitive_ability_score": cognitive_ability,
        "interest_alignment_score": interest_alignment,
        "motivation_clarity_score": motivation_clarity,
        "strength_discovery_score": strength_discovery,
        "career_readiness_score": career_readiness,
        "overall_career_intelligence": overall_career_intelligence,
        "priority_action": get_priority_action(scores),
        "recommended_pathways": get_recommended_pathways(interest_alignment, cognitive_ability, personality_trait),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    profile = args[0] if len(args) > 0 else "student-profile"
    assessment_type = args[1] if len(args) > 1 else "personality"
    personality_trait = int(args[2]) if len(args) > 2 else 82
    cognitive_ability = int(args[3]) if len(args) > 3 else 78
    interest_alignment = int(args[4]) if len(args) > 4 else 85
    motivation_clarity = int(args[5]) if len(args) > 5 else 74
    strength_discovery = int(args[6]) if len(args) > 6 else 88
    career_readiness = int(args[7]) if len(args) > 7 else 76

    result = analyze_career_intelligence(
        profile, assessment_type, personality_trait, cognitive_ability,
        interest_alignment, motivation_clarity, strength_discovery, career_readiness
    )

    print(f"Profile: {result['profile']}")
    print(f"Assessment Type: {result['assessment_type']}")
    print("=" * 45)
    print(f"Personality Trait Score:       {result['personality_trait_score']}/100  [{get_status(result['personality_trait_score'])}]")
    print(f"Cognitive Ability Score:       {result['cognitive_ability_score']}/100  [{get_status(result['cognitive_ability_score'])}]")
    print(f"Interest Alignment Score:      {result['interest_alignment_score']}/100  [{get_status(result['interest_alignment_score'])}]")
    print(f"Motivation Clarity Score:      {result['motivation_clarity_score']}/100  [{get_status(result['motivation_clarity_score'])}]")
    print(f"Strength Discovery Score:      {result['strength_discovery_score']}/100  [{get_status(result['strength_discovery_score'])}]")
    print(f"Career Readiness Score:        {result['career_readiness_score']}/100  [{get_status(result['career_readiness_score'])}]")
    print("=" * 45)
    print(f"Overall Career Intelligence:   {result['overall_career_intelligence']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nRecommended Career Pathways:")
    for pathway, score in result['recommended_pathways'].items():
        print(f"  {pathway:<28} {score}/100")


if __name__ == "__main__":
    main()
