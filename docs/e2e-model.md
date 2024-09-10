Imitation learning includes approaches such as,

- Behavioral Cloning (BC)
- Inverse Reinforcement Learning

This method involves training the model to minimize the difference between the predicted path (red line in the figure below) and the actual driving data (blue line in the figure below). The advantage of Behavioral Cloning is that it can be formulated as supervised learning on real driving data, making it easier to implement and compute compared to reinforcement learning and other approaches.

#### What are challenges in E2E autonomous driving?

covariate shift, meaning that data distribution during training differs from that during testing.

causal confusion

What are solutions to covariate shift?

Distorting Images

uses simulators that distort images to create pseudo-lateral deviations, allowing the model to learn behaviors to return to the original driving line. However, this method introduces the new problem of artificial artifacts due to image distortion. To resolve this, KL-divergence is introduced as a loss function to ensure that the distributions of distorted and original images are close in feature space.

Using NeRF and Gaussian Splatting

