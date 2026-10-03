# Duties and Responsibilities for Neural Architecture Latency Profiler Agent

## Dual-Control Architecture
Maker:
roofline-model-evaluator

Checker:
bandwidth-saturation-checker

## Operational Workflow
1. The Maker (roofline-model-evaluator) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (bandwidth-saturation-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
