"""calculate relevance between two sentences"""

import re
from typing import List, Any

def sentence_splitter(sentence: str) -> List[str]:
    """split the sentence into a sequence of words"""
    return re.findall(r'\b\w+\b', sentence.lower())

def longest_common_subsequence(a: List[Any], b: List[Any]) -> int:
    """return the length of the LCS"""
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[n][m]

def f1_score(recall: float, precision: float) -> float:
    """f1 score"""
    if precision + recall == 0:
        return 0.0

    return 2 * (precision * recall) / (precision + recall)

def relevanve_with_order(truth: List[Any], guess: List[Any]) -> float:
    """with order"""
    lcs_length = longest_common_subsequence(truth, guess)
    truth_length = len(truth)
    guess_length = len(guess)

    if guess_length == 0 or truth_length == 0:
        return 0.0

    precision = lcs_length / guess_length
    recall = lcs_length / truth_length

    return f1_score(recall, precision)


def relevanve_without_order(truth: List[Any], guess: List[Any]) -> float:
    """without order"""
    truth_set = set(truth)
    guess_set = set(guess)
    intersection = truth_set.intersection(guess_set)

    intersection_length = len(intersection)
    truth_length = len(truth_set)
    guess_length = len(guess_set)

    if guess_length == 0 or truth_length == 0:
        return 0.0

    precision = intersection_length / guess_length
    recall = intersection_length / truth_length

    return f1_score(recall, precision)

def sentencs_relevance_evaluator(truth: str, guess: str) -> tuple:
    """main"""
    truth_list = sentence_splitter(truth)
    guess_list = sentence_splitter(guess)
    return (relevanve_with_order(truth_list, guess_list), relevanve_without_order(truth_list, guess_list))
