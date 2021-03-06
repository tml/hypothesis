import hypothesis.strategytable as st
import hypothesis.searchstrategy as strat


def test_strategies_can_be_used_in_descriptors():
    intxfloat = st.StrategyTable.default().strategy((
        int, strat.ExponentialFloatStrategy()
    ))
    assert intxfloat.descriptor == (int, float)
