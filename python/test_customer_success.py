import pytest
from customer_success_balancing import CustomerSuccessBalancing

def build_scores(scores):
  return [{'id': index + 1, 'score': score} for index, score in enumerate(scores)]

class TestCustomerSuccessBalancing:
  def test_scenario_one(self):
    balancer = CustomerSuccessBalancing(
      build_scores([60, 20, 95, 75]),
      build_scores([90, 20, 70, 40, 60, 10]),
      [2, 4]
    )
    assert balancer.execute() == 1

  def test_scenario_two(self):
    balancer = CustomerSuccessBalancing(
      build_scores([11, 21, 31, 3, 4, 5]),
      build_scores([10, 10, 10, 20, 20, 30, 30, 30, 20, 60]),
      []
    )
    assert balancer.execute() == 0

  def test_scenario_three(self):
    balancer = CustomerSuccessBalancing(
      build_scores(list(range(1, 1000))),
      build_scores([998] * 10000),
      [999]
    )
    assert balancer.execute() == 998

  def test_scenario_four(self):
    balancer = CustomerSuccessBalancing(
      build_scores([1, 2, 3, 4, 5, 6]),
      build_scores([10, 10, 10, 20, 20, 30, 30, 30, 20, 60]),
      []
    )
    assert balancer.execute() == 0

  def test_scenario_five(self):
    balancer = CustomerSuccessBalancing(
      build_scores([100, 2, 3, 6, 4, 5]),
      build_scores([10, 10, 10, 20, 20, 30, 30, 30, 20, 60]),
      []
    )
    assert balancer.execute() == 1

  def test_scenario_six(self):
    balancer = CustomerSuccessBalancing(
      build_scores([100, 99, 88, 3, 4, 5]),
      build_scores([10, 10, 10, 20, 20, 30, 30, 30, 20, 60]),
      [1, 3, 2]
    )
    assert balancer.execute() == 0

  def test_scenario_seven(self):
    balancer = CustomerSuccessBalancing(
      build_scores([100, 99, 88, 3, 4, 5]),
      build_scores([10, 10, 10, 20, 20, 30, 30, 30, 20, 60]),
      [4, 5, 6]
    )
    assert balancer.execute() == 3

  def test_scenario_eight(self):
    balancer = CustomerSuccessBalancing(
      build_scores([60, 40, 95, 75]),
      build_scores([90, 70, 20, 40, 60, 10]),
      [2, 4]
    )
    assert balancer.execute() == 1

pytest.main()
