
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

# Your code goes here
page = st.sidebar.selectbox(label="Navigation", options=["Quicksort Visualizer"])

if page == "Quicksort Visualizer":
    st.sidebar.header("Array Configuration")
    array_size = st.sidebar.slider("Array Size", min_value=5, max_value=20, value=10)

    # Generate a random array
    arr = np.random.randint(1, 100, array_size)
    arr_copy = arr.copy() #create a copy to avoid modifying original array

    pivot_strategy = st.sidebar.selectbox("Pivot Selection Strategy", ["First", "Last", "Random"])

    steps = []  # Store the steps for visualization

    def partition(arr, low, high, pivot_strategy):
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

        else:  # Random pivot
            pivot_index = np.random.randint(low, high + 1)
            arr[high], arr[pivot_index] = arr[pivot_index], arr[high]  # Moving the pivot to the last position
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

    def quicksort(arr, low, high, pivot_strategy, steps):
        if low < high:
            pi = partition(arr, low, high, pivot_strategy)
            #st.write(arr) #printing array at each step of quicksort

            steps.append({"array": arr.copy(), "pivot": pi, "low": low, "high": high})  # Record step
            quicksort(arr, low, pi - 1, pivot_strategy, steps)
            quicksort(arr, pi + 1, high, pivot_strategy, steps)


    def visualize_step(arr, pivot_index=None, low=None, high=None):
        fig = go.Figure(data=[go.Bar(y=arr)])

        if pivot_index is not None:
            fig.add_trace(go.Scatter(x=[pivot_index], y=[arr[pivot_index]], mode='markers', marker=dict(size=20, color='red'), name='Pivot'))

        fig.update_layout(
            title=f"Quicksort Step",
            xaxis_title="Index",
            yaxis_title="Value",
            showlegend=False
        )
        return fig

    if st.button("Start Quicksort"):
        steps = []
        quicksort(arr_copy, 0, len(arr_copy) - 1, pivot_strategy, steps)

        for i, step in enumerate(steps):
            fig = visualize_step(step["array"], step["pivot"], step["low"], step["high"])
            st.plotly_chart(fig)
            time.sleep(0.5) #adding time delay to visualize the steps

# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
