## Prediction

Prediction provides future trajectories of observed movable objects. During planning, this information is processed and then future trajectory ego vehicle.

### Inputs to Prediction from Perception

- Object detection results (3D bounding boxes)
- Object classification
- Object tracking information
  - Position history
  - Velocity
  - Acceleration
  - Heading
 
- Scene context
  - Road structure
  - Traffic signs/signals
  - Weather conditions

- Actor attributes
  - Size
  - Type
  - Current state
 
- Map Features Used
  - Lane connectivity
  - Road geometry
  - Traffic rules
  - Semantic information
    - Speed limits
    - Turn restrictions
    - Stop lines
    - Crosswalks

4.2 Map-Based Constraints

Lane-following behavior
Legal maneuver checking
Road topology consideration
Speed profile generation
 
### Outputs to Planning

- Predicted trajectories
  - Multiple possible paths
  - Confidence scores
  - Time horizons (typically 3-8 seconds)

- Behavior predictions
  - Intent classification
  - Maneuver probabilities

- Risk assessment
  - Collision probabilities
  - Time-to-collision estimates

### Prediction methods

### Deep Learning-Based Methods

##### Transformer-Based Models
- Attention mechanisms for capturing interactions between actors
- Scene-transformer networks for multi-agent prediction
- GATO (Global Actor Trajectory Oracle) architecture

### Hybrid Approaches

#### Physics-Informed Neural Networks (PINNs)
- Combining physical constraints with deep learning
- Vehicle dynamics integration
- Road geometry considerations

### Probabilistic Methods

#### Multiple Hypothesis Prediction
- Generation of multiple possible trajectories
- Probability distribution over future states
- Uncertainty quantification


### Prediction metrics

The most common prediction quality measures are,
- Average Displacement Error (ADE - mean L2 distance between all trajectory points)
- Final Displacement Error (FDE - L2 distance between final trajectory points)











### Refrences
- [Why ADE and FDE are not the best metrics to score motion prediction](https://towardsdatascience.com/why-ade-and-fde-might-not-be-the-best-metrics-to-score-motion-prediction-model-performance-and-what-1980366d37be)
