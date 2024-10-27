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

## Models

# State-of-the-Art Motion Prediction Models

## 1. SceneTransformer (2023)
### Architecture
- Multi-head attention-based architecture
- Scene-centric representation learning
- Multiple parallel transformer blocks

### Working Principle
1. **Input Processing**
   ```
   - Historical trajectories (past 2-3 seconds)
   - Scene context vectors
   - Agent-to-agent relationships
   ```

2. **Scene Encoding**
   - Converts raw inputs into learned embeddings
   - Combines spatial and temporal information
   - Maintains relative positioning

3. **Cross-Attention Mechanism**
   ```python
   # Pseudo-code representation
   class SceneTransformer:
       def process(self, scene):
           agent_features = self.encode_agents(scene.agents)
           map_features = self.encode_map(scene.map)
           
           # Multi-head attention
           attention_weights = self.attention(
               query=agent_features,
               key=map_features,
               value=map_features
           )
           
           # Scene-level reasoning
           scene_context = self.scene_transformer(
               agent_features, 
               attention_weights
           )
   ```

### Key Features
- Multi-modal prediction output
- Handles variable number of agents
- Explicit modeling of interactions
- Scene-level reasoning

## 2. LaneGCN (Latest Version)
### Architecture
- Graph Neural Network based
- Lane-centric representation
- Hierarchical feature extraction

### Working Principle
1. **Lane Graph Construction**
   - Nodes: Lane segments
   - Edges: Lane connections
   - Features: Road attributes

2. **Message Passing**
   ```python
   # Conceptual implementation
   class LaneGCN:
       def forward(self, lane_graph, agents):
           # Lane-level features
           lane_features = self.lane_encoder(lane_graph)
           
           # Actor-to-lane attention
           actor_lane_attention = self.compute_attention(
               agents, 
               lane_features
           )
           
           # Update actor features
           actor_features = self.update_features(
               agents,
               actor_lane_attention,
               lane_features
           )
   ```

3. **Trajectory Generation**
   - Multi-scale feature aggregation
   - Lane-based anchoring
   - Multiple trajectory hypotheses

### Advantages
- Strong lane-following behavior
- Efficient computation
- Interpretable predictions
- Map-aware predictions

## 3. MultiPath++ (2023)
### Architecture
- Anchor-based trajectory prediction
- Multi-modal output generation
- Scene context integration

### Working Principle
1. **Trajectory Anchors**
   - Pre-defined trajectory patterns
   - Learned from data
   - Coverage of common behaviors

2. **Feature Extraction**
   ```python
   class MultiPathPlusPlus:
       def extract_features(self, scene):
           # Agent history encoding
           agent_history = self.encode_history(
               scene.agent_trajectories
           )
           
           # Scene context
           scene_features = self.encode_context(
               scene.map,
               scene.traffic
           )
           
           # Anchor scoring
           scores = self.score_anchors(
               agent_history,
               scene_features
           )
   ```

3. **Trajectory Refinement**
   - Anchor modification
   - Uncertainty estimation
   - Mode selection

### Key Features
- Fast inference
- Interpretable outputs
- Handles multiple modes
- Scene-aware predictions

## 4. PRIME (Prediction In Motion Environments)
### Architecture
- Hierarchical structure
- Intent-aware prediction
- Multi-agent modeling

### Working Principle
1. **Intent Recognition**
   - Goal estimation
   - Behavior classification
   - Route planning

2. **Interaction Modeling**
   ```python
   class PRIME:
       def model_interactions(self, agents):
           # Pairwise interaction features
           interactions = self.compute_interactions(agents)
           
           # Global context
           global_context = self.aggregate_context(
               interactions
           )
           
           # Update agent states
           updated_states = self.update_agents(
               agents,
               interactions,
               global_context
           )
   ```

3. **Trajectory Generation**
   - Multi-modal outputs
   - Probabilistic sampling
   - Safety constraints

### Advanced Features
- Real-time performance
- Uncertainty quantification
- Social compliance
- Goal-oriented prediction

## 5. Implementation Considerations

### 1. Data Pipeline
```python
def prepare_data(raw_data):
    # Historical trajectories
    past_trajectories = extract_history(raw_data)
    
    # Map features
    map_features = process_map(raw_data.map)
    
    # Dynamic objects
    dynamic_features = process_dynamic_objects(raw_data)
    
    return {
        'trajectories': past_trajectories,
        'map': map_features,
        'dynamic': dynamic_features
    }
```

### 2. Training Strategy
```python
def train_model(model, data_loader):
    for epoch in range(num_epochs):
        for batch in data_loader:
            # Forward pass
            predictions = model(batch)
            
            # Multiple loss components
            regression_loss = compute_regression_loss(
                predictions.trajectories,
                batch.ground_truth
            )
            
            classification_loss = compute_classification_loss(
                predictions.modes,
                batch.actual_modes
            )
            
            # Update model
            total_loss = regression_loss + classification_loss
            total_loss.backward()
```

### 3. Inference Pipeline
```python
def inference(model, scene):
    # Preprocess scene
    features = prepare_data(scene)
    
    # Generate predictions
    predictions = model(features)
    
    # Post-process
    trajectories = filter_trajectories(predictions)
    
    return {
        'trajectories': trajectories,
        'probabilities': predictions.probabilities,
        'modes': predictions.modes
    }
```




### Prediction metrics

The most common prediction quality measures are,
- Average Displacement Error (ADE - mean L2 distance between all trajectory points)
- Final Displacement Error (FDE - L2 distance between final trajectory points)











### Refrences
- [Why ADE and FDE are not the best metrics to score motion prediction](https://towardsdatascience.com/why-ade-and-fde-might-not-be-the-best-metrics-to-score-motion-prediction-model-performance-and-what-1980366d37be)
