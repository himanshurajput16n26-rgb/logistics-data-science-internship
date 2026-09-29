# Week 1 Research Notes

## Scenario

A hypothetical omnichannel logistics company receives customer orders, fulfils them through distribution operations, and delivers orders using multiple shipping modes and regional logistics partners.

The analytical objective is to improve service reliability and resource allocation.

## Key Problems

- Late deliveries
- Uneven workload
- Capacity allocation
- Route planning
- Demand uncertainty
- Different service performance across regions/shipping modes

## Data Source

DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS

Mendeley Data:
https://data.mendeley.com/datasets/8gx2fvg2k6/5

## Analytical Methods

### Descriptive Analytics
Used to establish KPI baselines and identify trends.

### Classification
Used to predict whether an order is likely to be late.

### Regression
Used for continuous outcomes such as shipping duration or expected workload.

### Forecasting
Used to estimate future order/shipment volumes.

### Clustering
Used to identify groups of similar customers, orders, or regions.

### Optimization
A Vehicle Routing Problem with Time Windows (VRPTW) can be used to allocate deliveries to vehicles subject to capacity and delivery-window constraints.

## Leakage Control

A pre-delivery model must not use information that becomes available only after delivery. For example, actual delivery date and final delivery duration should not be used to predict whether that same delivery will be late.

## References

- https://data.mendeley.com/datasets/8gx2fvg2k6/5
- https://scikit-learn.org/
- https://developers.google.com/optimization/routing
- https://developers.google.com/optimization/routing/vrptw
