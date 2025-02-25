# tanh-neural-network
### Clear Steps of How the Code Works:

1. **Define the Activation Function**  
   - The `tanh` function is implemented to process values in the neural network.

2. **Initialize Weights Randomly**  
   - Each weight is set to a random value between \([-0.5, 0.5]\).

3. **Set Bias Values**  
   - The biases are set as `b1 = 0.5` and `b2 = 0.7`.

4. **Define Input Values**  
   - The input values are set to `x1 = 0.3` and `x2 = -0.2`.

5. **Set the Target Output and Conditions**  
   - The network should aim to produce `0.8` as output, with an acceptable error of `0.01`.

6. **Start a Training Loop**  
   - The loop keeps running until the network's output is close enough to the target.

7. **Calculate Hidden Layer Outputs**  
   - The weighted sum of inputs is computed for two hidden neurons.  
   - The `tanh` function is applied to these sums.

8. **Compute the Final Output**  
   - The hidden layer outputs are combined to produce the final output using another weighted sum and `tanh`.

9. **Check if the Output is Close Enough**  
   - If the output is within `0.01` of the target, the loop stops.

10. **Adjust Weights Randomly**  
   - If the output is not close enough, each weight is slightly adjusted.

11. **Repeat Until the Desired Output is Achieved**  
   - The process continues until the network's output is close enough to `0.8`.

12. **Print the Final Output**  
   - Once the training stops, the final output is displayed.
