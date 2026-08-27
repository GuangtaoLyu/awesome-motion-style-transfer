# -*- coding: utf-8 -*-
"""Per-repo classifier for awesome-motion-style-transfer.

Rule order matters: most specific categories first. A paper is assigned the
first category whose keyword appears in its title/venue. Falls back to the
config default (core Motion Style Transfer).
"""
from lib_common import classify_by_rules

RULES = [
    ("Surveys", ["survey", "review of", "a review"]),
    ("Datasets & Benchmarks", ["dataset", "benchmark", "benchmarking"]),
    ("Motion Retargeting & Imitation",
     ["retarget", "imitation", "mimic", "kinematic transfer", "motion copying",
      "motion retargeting"]),
    ("Stylized Motion Generation",
     ["stylized", "style-based", "style conditioned", "style-conditioned",
      "style-guided", "motion stylization", "stylized generation",
      "style-controllable"]),
    ("Motion Style Transfer",
     ["style transfer", "motion style", "style transfer for human",
      "human motion style"]),
]

DEFAULT = "Motion Style Transfer"


def classify(paper, config=None):
    return classify_by_rules(paper, RULES, DEFAULT)
