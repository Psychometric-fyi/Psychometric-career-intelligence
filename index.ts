#!/usr/bin/env node

interface IntelInput {
  profile: string;
  assessmentType: string;
  personalityTrait: number;
  cognitiveAbility: number;
  interestAlignment: number;
  motivationClarity: number;
  strengthDiscovery: number;
  careerReadiness: number;
}

interface IntelOutput {
  profile: string;
  assessmentType: string;
  personalityTraitScore: number;
  cognitiveAbilityScore: number;
  interestAlignmentScore: number;
  motivationClarityScore: number;
  strengthDiscoveryScore: number;
  careerReadinessScore: number;
  overallCareerIntelligence: number;
  priorityAction: string;
  recommendedPathways: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    personalityTrait: "Personality Trait",
    cognitiveAbility: "Cognitive Ability",
    interestAlignment: "Interest Alignment",
    motivationClarity: "Motivation Clarity",
    strengthDiscovery: "Strength Discovery",
    careerReadiness: "Career Readiness",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getRecommendedPathways(interest: number, cognitive: number, personality: number): Record<string, number> {
  return {
    "STEM & Technology": Math.min(100, Math.round(cognitive * 1.05)),
    "Creative & Design": Math.min(100, Math.round(personality * 0.95)),
    "Business & Leadership": Math.min(100, Math.round(interest * 1.0)),
    "Social & Education": Math.min(100, Math.round((personality + interest) / 2)),
  };
}

export function analyzeCareerIntelligence(input: IntelInput): IntelOutput {
  const scores = {
    personalityTrait: input.personalityTrait,
    cognitiveAbility: input.cognitiveAbility,
    interestAlignment: input.interestAlignment,
    motivationClarity: input.motivationClarity,
    strengthDiscovery: input.strengthDiscovery,
    careerReadiness: input.careerReadiness,
  };
  const overallCareerIntelligence = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    profile: input.profile,
    assessmentType: input.assessmentType.charAt(0).toUpperCase() + input.assessmentType.slice(1),
    personalityTraitScore: input.personalityTrait,
    cognitiveAbilityScore: input.cognitiveAbility,
    interestAlignmentScore: input.interestAlignment,
    motivationClarityScore: input.motivationClarity,
    strengthDiscoveryScore: input.strengthDiscovery,
    careerReadinessScore: input.careerReadiness,
    overallCareerIntelligence,
    priorityAction: getPriorityAction(scores),
    recommendedPathways: getRecommendedPathways(input.interestAlignment, input.cognitiveAbility, input.personalityTrait),
  };
}

const args = process.argv.slice(2);
const profile = args[0] || "student-profile";
const assessmentType = args[1] || "personality";
const personalityTrait = parseInt(args[2]) || 82;
const cognitiveAbility = parseInt(args[3]) || 78;
const interestAlignment = parseInt(args[4]) || 85;
const motivationClarity = parseInt(args[5]) || 74;
const strengthDiscovery = parseInt(args[6]) || 88;
const careerReadiness = parseInt(args[7]) || 76;

const result = analyzeCareerIntelligence({
  profile, assessmentType, personalityTrait, cognitiveAbility,
  interestAlignment, motivationClarity, strengthDiscovery, careerReadiness,
});

console.log(`Profile: ${result.profile}`);
console.log(`Assessment Type: ${result.assessmentType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Personality Trait Score:       ${result.personalityTraitScore}/100  [${getStatus(result.personalityTraitScore)}]`);
console.log(`Cognitive Ability Score:       ${result.cognitiveAbilityScore}/100  [${getStatus(result.cognitiveAbilityScore)}]`);
console.log(`Interest Alignment Score:      ${result.interestAlignmentScore}/100  [${getStatus(result.interestAlignmentScore)}]`);
console.log(`Motivation Clarity Score:      ${result.motivationClarityScore}/100  [${getStatus(result.motivationClarityScore)}]`);
console.log(`Strength Discovery Score:      ${result.strengthDiscoveryScore}/100  [${getStatus(result.strengthDiscoveryScore)}]`);
console.log(`Career Readiness Score:        ${result.careerReadinessScore}/100  [${getStatus(result.careerReadinessScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Career Intelligence:   ${result.overallCareerIntelligence}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nRecommended Career Pathways:");
Object.entries(result.recommendedPathways).forEach(([pathway, score]) => {
  console.log(`  ${pathway.padEnd(26)} ${score}/100`);
});
