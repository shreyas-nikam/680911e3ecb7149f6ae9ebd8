
# Technical Specifications for a Streamlit Quicksort Visualizer Application

## Overview

This document outlines the technical specifications for a Streamlit application designed to visualize the Quicksort algorithm. The application will allow users to input a synthetic array, select a pivot selection strategy, and step through the sorting process, observing the changes in the array at each step.  This application focuses on demonstrating the "divide-and-conquer" strategy fundamental to Quicksort.

## Step-by-Step Generation Process

1.  **Project Setup:**
    *   Create a new Python project directory.
    *   Create a virtual environment.
    *   Install the necessary libraries (Streamlit, NumPy, and potentially Matplotlib or Plotly for visualization).

2.  **Import Libraries:**
    ```python
    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt  # Or import plotly.express as px
    ```

3.  **User Input and Initialization:**
    *   Create a Streamlit sidebar to allow users to define the array size or enter a custom array as a comma-separated string.
    *   Provide a dropdown to select the pivot selection strategy (First, Last, Random).
    *   Generate a synthetic array using NumPy if the user specifies array size. Otherwise, parse the user-provided string into an array.

    ```python
    st.sidebar.header("Array Configuration")
    array_size = st.sidebar.slider("Array Size", min_value=5, max_value=20, value=10) #Using slider for array size

    # Generate a random array
    arr = np.random.randint(1, 100, array_size) #Random Integers in range 1 to 100

    pivot_strategy = st.sidebar.selectbox("Pivot Selection Strategy", ["First", "Last", "Random"])
    ```

4.  **Quicksort Implementation:**
    *   Implement the Quicksort algorithm with a partition function.
    *   Modify the partition function to highlight the elements being compared and swapped.
    *   Store each step of the sorting process (array state, pivot, highlighted elements) in a list for later visualization.

    ```python
    def partition(arr, low, high, pivot_strategy, steps):
        if pivot_strategy == "First":
            pivot = arr[low]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while arr[i] < pivot:
                    i += 1
                j -= 1
                while arr[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                arr[i], arr[j] = arr[j], arr[i]

        elif pivot_strategy == "Last":
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1


        else: # Random pivot
            pivot_index = np.random.randint(low, high+1)
            pivot = arr[pivot_index]
            arr[high], arr[pivot_index] = arr[pivot_index], arr[high] #Moving the pivot to the last position
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

    def quicksort(arr, low, high, pivot_strategy, steps):
        if low < high:
            pi = partition(arr, low, high, pivot_strategy, steps)
            quicksort(arr, low, pi - 1, pivot_strategy, steps)
            quicksort(arr, pi + 1, high, pivot_strategy, steps)
    ```

5.  **Visualization:**
    *   Create a function to visualize the array at each step using `matplotlib.pyplot` or `plotly.express`.
    *   Use bar charts to represent the array elements.
    *   Highlight the pivot element and elements being compared/swapped using different colors.
    *   Display the relevant part of the Quicksort pseudocode alongside the visualization, updating it for each step.
    *   Use `st.pyplot()` or `st.plotly_chart()` to display the visualizations in the Streamlit app.

    ```python
    def visualize_step(arr, pivot_index=None, compared_indices=None, swapped_indices=None):
        fig, ax = plt.subplots()
        ax.bar(range(len(arr)), arr)

        if pivot_index is not None:
            ax.patches[pivot_index].set_facecolor('red')  # Highlight pivot

        if compared_indices:
            for idx in compared_indices:
                ax.patches[idx].set_facecolor('yellow')  # Highlight compared

        if swapped_indices:
            for idx in swapped_indices:
                ax.patches[idx].set_facecolor('green')  # Highlight swapped

        st.pyplot(fig)
    ```

6.  **Interactive Control:**
    *   Use Streamlit buttons (`st.button()`) to control the execution of the algorithm, allowing users to step forward and backward through the sorting process.
    *   Display the current step number.
    *   Implement a "Reset" button to start the visualization from the beginning with a new array.

7.  **Documentation and Annotations:**
    *   Add tooltips and inline help using `st.help()` or `st.markdown()` to explain each step of the sorting process.
    *   Provide a brief explanation of the Quicksort algorithm and its "divide-and-conquer" strategy at the beginning of the application.

8.  **Main Application Loop:**
    *   Orchestrate the application flow by handling user input, executing the Quicksort algorithm, and displaying the visualizations.

    ```python
    if st.button("Start Quicksort"):
        steps = []
        arr_copy = arr.copy()
        quicksort(arr_copy, 0, len(arr_copy) - 1, pivot_strategy, steps)
        for i in range(len(steps)):
            visualize_step(steps[i]["array"], steps[i]["pivot"], steps[i]["compared"], steps[i]["swapped"])
    ```

## Important Definitions, Examples, and Formulae

*   **Quicksort Algorithm:** A divide-and-conquer sorting algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.

*   **Divide-and-Conquer:** A problem-solving paradigm where a problem is broken down into smaller subproblems of the same type, solved recursively, and their solutions are combined to solve the original problem. Quicksort exemplifies this by recursively partitioning the array.

*   **Pivot Selection:** The process of choosing an element from the array to be used as the pivot during partitioning.  Different strategies exist:
    *   **First Element:**  Selecting the first element of the array.
    *   **Last Element:**  Selecting the last element of the array.
    *   **Random Element:**  Selecting a random element from the array.

*   **Partitioning:** The process of rearranging the elements of the array such that all elements less than the pivot are placed before the pivot, and all elements greater than the pivot are placed after it.

*   **Recursion:** The process where a function calls itself within its own definition. Quicksort uses recursion to sort the sub-arrays created during partitioning.

*   **Time Complexity:**
    *   **Best Case:** O(n log n) - Occurs when the pivot divides the array into nearly equal partitions.
    *   **Average Case:** O(n log n) -  On average, Quicksort performs well.
    *   **Worst Case:** O(n^2) - Occurs when the pivot consistently results in highly unbalanced partitions (e.g., pivot is always the smallest or largest element).

## Libraries and Tools

*   **Streamlit:** Used for building the interactive web application. It provides widgets, layout elements, and mechanisms for displaying data and visualizations.

    *   `st.sidebar`: Creates a sidebar for user inputs.
    *   `st.slider`: Creates a slider for numerical input (array size).
    *   `st.selectbox`: Creates a dropdown menu for selecting the pivot strategy.
    *   `st.button`: Creates a button to trigger the sorting process.
    *   `st.pyplot`: Displays Matplotlib plots in the Streamlit application.
    *   `st.markdown`: For displaying text, including descriptions and explanations.
    *   `st.help`: For providing inline help and tooltips.
*   **NumPy:** Used for generating the synthetic array and performing array manipulations.

    *   `np.random.randint`: Generates random integers for the array elements.
*   **Matplotlib (or Plotly):** Used for creating the visualizations of the array during the sorting process.

    *   `matplotlib.pyplot.bar`: Creates bar charts to represent the array elements.
    *   `matplotlib.pyplot.subplots`: Creates a figure and axes for the plot.
    *   Plotly offers similar chart types but can be more interactive, especially when combined with Streamlit.  `plotly.express.bar` would be used for an interactive bar chart in Plotly.


### Appendix Code

```code
function quicksort(A, low, high):
if low < high:
pivotIndex = partition(A, low, high)
quicksort(A, low, pivotIndex - 1)
quicksort(A, pivotIndex + 1, high)

function partition(A, low, high):
pivot = A[high]
# Choose last element as pivot
i = low - 1
for j = low to high - 1:
if A[j] <= pivot:
i = i + 1
swap(A[i], A[j])
swap(A[i + 1], A[high])
return i + 1
# Place pivot at correct position
```