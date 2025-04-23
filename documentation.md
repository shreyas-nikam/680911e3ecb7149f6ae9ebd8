id: 680911e3ecb7149f6ae9ebd8_documentation
summary: Lab for successful run Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab Codelab: Visualizing Quicksort

This codelab will guide you through the "QuLab" Streamlit application, focusing on the "Quicksort Visualizer" functionality. Quicksort is a highly efficient sorting algorithm, and this application provides an interactive way to understand its inner workings. By the end of this codelab, you'll understand how to configure the visualizer, select different pivot strategies, and trace the execution of the Quicksort algorithm step by step. This application will help you to visualize and deeply understand the Quicksort algorithm.

## Setting up the Environment
Duration: 00:05

Before you begin, ensure you have the following:

*   Python 3.6 or higher installed.
*   Streamlit installed (`pip install streamlit`).
*   Libraries such as numpy and plotly installed (`pip install numpy plotly`).

## Running the Application
Duration: 00:02

1.  Save the provided code as `app.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved `app.py`.
4.  Run the application using the command: `streamlit run app.py`

This will automatically open the application in your web browser.

## Exploring the User Interface
Duration: 00:05

The application's user interface consists of:

*   **Sidebar:**  Used for navigation and configuring the quicksort visualization. It includes:
    *   A navigation selectbox to choose between different functionalities (currently only "Quicksort Visualizer").
    *   A header "Array Configuration" with controls for setting the array size and pivot selection strategy.
    *   A "Start Quicksort" button to initiate the visualization.
*   **Main Area:** Displays the title "QuLab", visual representations of the Quicksort algorithm's steps, and copyright information.

## Configuring the Array
Duration: 00:05

The sidebar provides options to configure the array that will be sorted.

1.  **Array Size:**  Use the slider to select the number of elements in the array. The slider ranges from 5 to 20 elements. The default value is 10.
2.  **Pivot Selection Strategy:**  Choose one of the following strategies for selecting the pivot element in each partition:
    *   **First:** The first element of the partition is selected as the pivot.
    *   **Last:** The last element of the partition is selected as the pivot.
    *   **Random:** A random element within the partition is selected as the pivot.

<aside class="positive">
Selecting different pivot strategies can significantly impact the performance of Quicksort. Experimenting with these strategies can help you understand the best and worst-case scenarios for Quicksort.
</aside>

## Understanding the Code: `partition` Function
Duration: 00:15

The `partition` function is the heart of the Quicksort algorithm. It rearranges the array such that all elements less than the pivot are placed before it, and all elements greater than the pivot are placed after it.

Here's a breakdown:

*   **Input:**
    *   `arr`: The array to be partitioned.
    *   `low`: The starting index of the partition.
    *   `high`: The ending index of the partition.
    *   `pivot_strategy`: The chosen pivot selection strategy.

*   **Logic:**
    *   The function implements different partitioning logic based on the `pivot_strategy`.

    *   **First Pivot:**
        *   The first element `arr[low]` is chosen as pivot.
        *   `i` starts from `low - 1` and `j` starts from `high + 1`.
        *   Increment `i` until `arr[i]` is greater than or equal to the `pivot`.
        *   Decrement `j` until `arr[j]` is less than or equal to the `pivot`.
        *   If `i` is greater than or equal to `j`, the function returns `j`.
        *   Otherwise swap `arr[i]` and `arr[j]`.

    *   **Last Pivot:**
        *   The last element `arr[high]` is chosen as pivot.
        *   `i` is initialized to `low - 1`.
        *   The array is iterated from `low` to `high-1`.
        *   If an element `arr[j]` is less than or equal to the `pivot`, `i` is incremented and `arr[i]` and `arr[j]` are swapped.
        *   Finally, `arr[i+1]` and `arr[high]` are swapped to place the pivot at its correct position.
        *   The function returns `i + 1` which is the index of pivot.

    *   **Random Pivot:**
        *   A random index is selected between `low` and `high` (inclusive).
        *   The element at the random index is swapped with the last element to use the last element pivot implementation.
        *   The rest of the logic is the same as last pivot strategy.

*   **Output:** The index of the pivot element after partitioning.

## Understanding the Code: `quicksort` Function
Duration: 00:10

The `quicksort` function is a recursive function that applies the "divide and conquer" strategy to sort the array.

*   **Input:**
    *   `arr`: The array to be sorted.
    *   `low`: The starting index of the subarray to be sorted.
    *   `high`: The ending index of the subarray to be sorted.
    *   `pivot_strategy`:  The pivot selection strategy.
    *   `steps`: A list to store the state of the array at each step.

*   **Logic:**
    1.  **Base Case:** If `low` is not less than `high`, the subarray is either empty or contains only one element, which is already sorted.
    2.  **Partition:** Call the `partition` function to partition the array around a pivot element.
    3.  **Record Step:** Append a copy of the array along with the pivot index, low and high indices to the `steps` list. This is crucial for visualizing the sorting process.
    4.  **Recursive Calls:** Recursively call `quicksort` on the two subarrays:
        *   From `low` to `pi - 1` (elements before the pivot).
        *   From `pi + 1` to `high` (elements after the pivot).

## Understanding the Code: `visualize_step` Function
Duration: 00:10

The `visualize_step` function takes an array and optionally a pivot index and creates a bar chart using Plotly to visualize the array's state at a particular step.

*   **Input:**
    *   `arr`: The array to be visualized.
    *   `pivot_index`: The index of the pivot element (optional).
    *   `low`: The starting index of the partition (optional).
    *   `high`: The ending index of the partition (optional).

*   **Logic:**
    1.  Creates a bar chart of the input array.
    2.  If a `pivot_index` is provided, it adds a marker to highlight the pivot element in red.
    3.  Sets the title and axis labels for the chart.

*   **Output:** A Plotly figure representing the visualized step.

## Running the Visualization
Duration: 00:10

1.  Configure the array size and pivot selection strategy using the sidebar controls.
2.  Click the "Start Quicksort" button.

The application will then execute the Quicksort algorithm and display a series of bar charts, each representing a step in the sorting process. The pivot element for each step is highlighted in red.  The `time.sleep(0.5)` introduces a short delay between each step, allowing you to follow the algorithm's progress visually.

<aside class="negative">
Be mindful of the array size when running the visualization. Larger arrays will take longer to sort, and the visualization may become less clear.
</aside>

## Code Architecture
Duration: 00:10

Here's a high-level overview of the application's architecture:

```
graph LR
    A[User Interaction (Streamlit UI)] --> B(Configuration (Array Size, Pivot Strategy));
    B --> C{Start Quicksort Button};
    C -- Clicked --> D(Array Generation);
    D --> E(Quicksort Algorithm);
    E -- Step --> F(Visualize Step);
    F --> G[Display (Plotly Chart)];
    E -- Complete --> H[End];
```

*   The user interacts with the Streamlit UI to configure the array size and pivot selection strategy.
*   Clicking the "Start Quicksort" button triggers the array generation.
*   The Quicksort algorithm is executed. At each step, the current state of the array is visualized using Plotly.
*   The Plotly chart is displayed in the main area of the Streamlit application.
*   The process continues until the array is fully sorted.

## Further Exploration
Duration: 00:05

*   Experiment with different array sizes and pivot selection strategies to observe their impact on the Quicksort algorithm's performance.
*   Modify the code to display additional information, such as the number of comparisons or swaps performed at each step.
*   Implement other sorting algorithms and visualize them using the same framework.

This codelab provided a comprehensive guide to the QuLab application's Quicksort Visualizer. You should now have a solid understanding of how the application works and how to use it to visualize the Quicksort algorithm.
