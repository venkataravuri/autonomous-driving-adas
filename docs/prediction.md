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



# Anchor-Based Trajectory Prediction: A Deep Dive

## 1. Core Concept
Anchor-based trajectory prediction uses pre-defined trajectory patterns (anchors) as templates to predict future vehicle movements. Think of these anchors as "prototype trajectories" that serve as starting points for prediction.

## 2. How It Works

### 2.1 Anchor Generation
```python
class AnchorGenerator:
    def generate_anchors(self, num_anchors=64):
        anchors = []
        # Generate diverse trajectory patterns
        for i in range(num_anchors):
            # Each anchor is a sequence of (x, y) coordinates
            anchor = {
                'points': [(x1, y1), (x2, y2), ..., (xn, yn)],
                'pattern_type': 'lane_follow/lane_change/turn',
                'probability': initial_probability
            }
            anchors.append(anchor)
        return anchors
```

### 2.2 Types of Anchors
1. **Lane-Following Anchors**
   - Straight trajectories
   - Curved paths following lane geometry
   - Different speeds and accelerations

2. **Lane-Change Anchors**
   - Left and right lane changes
   - Various completion times
   - Different lateral velocities

3. **Turn Anchors**
   - Left and right turns
   - Different turning radii
   - Various entry/exit speeds

### 2.3 Anchor Selection and Refinement

```python
class AnchorPredictor:
    def predict(self, vehicle_state, anchors, scene_context):
        # 1. Score each anchor
        anchor_scores = []
        for anchor in anchors:
            score = self.compute_anchor_score(
                vehicle_state,
                anchor,
                scene_context
            )
            anchor_scores.append(score)
        
        # 2. Select top-k anchors
        top_k_anchors = self.select_top_k(
            anchors,
            anchor_scores,
            k=6
        )
        
        # 3. Refine selected anchors
        refined_trajectories = []
        for anchor in top_k_anchors:
            refined = self.refine_anchor(
                anchor,
                vehicle_state,
                scene_context
            )
            refined_trajectories.append(refined)
        
        return refined_trajectories
```

## 3. Key Components

### 3.1 Anchor Library
- Pre-computed from large-scale driving data
- Covers common driving scenarios
- Regularly updated based on new data

### 3.2 Scoring Mechanism
```python
def compute_anchor_score(self, vehicle_state, anchor, scene_context):
    # Factors considered in scoring:
    scores = {
        'kinematic_feasibility': self.check_kinematics(
            vehicle_state, 
            anchor
        ),
        'map_compliance': self.check_map_compliance(
            anchor, 
            scene_context.map
        ),
        'collision_risk': self.assess_collision_risk(
            anchor, 
            scene_context.other_agents
        ),
        'behavior_naturalness': self.evaluate_naturalness(
            anchor, 
            scene_context
        )
    }
    
    return self.weighted_score(scores)
```

### 3.3 Refinement Process
1. **Initial Alignment**
   - Match anchor start point with current vehicle state
   - Adjust orientation to match current heading

2. **Context Adaptation**
   ```python
   def refine_anchor(self, anchor, vehicle_state, scene_context):
       # Start with basic alignment
       aligned = self.align_to_vehicle(anchor, vehicle_state)
       
       # Adapt to road geometry
       geometry_adjusted = self.adapt_to_road(
           aligned, 
           scene_context.map
       )
       
       # Consider dynamic obstacles
       obstacle_adjusted = self.avoid_obstacles(
           geometry_adjusted,
           scene_context.obstacles
       )
       
       # Apply physical constraints
       physically_feasible = self.apply_vehicle_dynamics(
           obstacle_adjusted,
           vehicle_state
       )
       
       return physically_feasible
   ```

## 4. Advantages and Challenges

### 4.1 Advantages
1. **Computational Efficiency**
   - Pre-computed anchors reduce computation time
   - Parallel processing of multiple anchors
   - Fast real-time performance

2. **Interpretability**
   - Clear connection to common driving patterns
   - Explainable prediction choices
   - Easy to validate and debug

3. **Robustness**
   - Built-in physical constraints
   - Realistic trajectories by design
   - Handles common scenarios well

### 4.2 Challenges
1. **Coverage Limitations**
   - May miss unusual scenarios
   - Finite number of anchors
   - Discretization effects

2. **Refinement Complexity**
   ```python
   def handle_edge_cases(self, anchor, scene):
       # Example of handling complex scenarios
       if self.is_unusual_scenario(scene):
           # Generate custom anchor
           custom_anchor = self.generate_custom_anchor(scene)
           return self.blend_anchors(anchor, custom_anchor)
       return anchor
   ```

## 5. Implementation Best Practices

### 5.1 Anchor Selection
- Use hierarchical clustering for anchor library generation
- Maintain diverse anchor set
- Regular update based on new data

### 5.2 Performance Optimization
```python
class OptimizedPredictor:
    def __init__(self):
        # Cache frequently used anchors
        self.anchor_cache = LRUCache(1000)
        
    def predict_with_caching(self, state):
        cache_key = self.compute_cache_key(state)
        if cache_key in self.anchor_cache:
            return self.refine_cached_prediction(
                self.anchor_cache[cache_key],
                state
            )
        
        # Full prediction if not in cache
        prediction = self.full_prediction(state)
        self.anchor_cache[cache_key] = prediction
        return prediction
```








### Refrences
- [Why ADE and FDE are not the best metrics to score motion prediction](https://towardsdatascience.com/why-ade-and-fde-might-not-be-the-best-metrics-to-score-motion-prediction-model-performance-and-what-1980366d37be)
