# Animating Worst-Case Merge Sort with Manim

This project visualizes the worst-case scenario of the Merge Sort algorithm using the Manim animation library. Understanding the worst-case performance of sorting algorithms is crucial for efficient algorithm design and selection. This animation aims to provide an intuitive understanding of how Merge Sort behaves in its least optimal scenario.

## Purpose

The primary goal of this project is to:

* Visually demonstrate the steps involved in the Merge Sort algorithm when it encounters its worst-case input.
* Illustrate the time complexity implications of the worst-case scenario.
* Serve as an educational tool for students and anyone interested in learning about sorting algorithms and their performance characteristics.
* Showcase the capabilities of the Manim library for creating engaging mathematical and algorithmic visualizations.


Merge Sort has a consistent time complexity of O(n log n) in all cases (best, average, and worst). However, the number of comparisons and the visual representation of the merge steps can differ. The worst-case scenario for the animation (in terms of visual complexity and potentially the number of comparisons, though the overall time complexity remains the same) often occurs when the input array is inversely sorted or when elements are arranged in a way that maximizes the number of individual element comparisons during the merge steps.

This animation specifically focuses on visualizing the splitting and merging process in a scenario designed to represent this less optimal arrangement visually.


The project directory is organized as follows:

![image](https://github.com/user-attachments/assets/9e72226a-0378-4d07-984b-77cd0ed061c7)


* **`environment.txt`**: This file contains the necessary Python packages and versions required to run the project, including Manim.
* **`media/`**: This top-level directory is intended for general project media like images, texts, and potentially final video outputs.
* **`Merge_sort/`**: This subdirectory contains the specific files related to the Merge Sort animation.
    * **`Merge_sort/media/`**: This subdirectory within `Merge_sort` might contain specific media assets needed for the animation defined in `merge_animation.py`.
    * **`Merge_sort/merge_animation.py`**: This Python file contains the Manim code that defines and generates the Merge Sort animation.


Before running the animation, ensure you have the necessary environment set up. This likely involves:

1.  **Installing Python:** Manim requires Python 3.7 or higher.
2.  **Installing Manim:** Follow the installation instructions provided in the official Manim documentation (typically involving pip).
3.  **Installing Dependencies:** The `environment.txt` file lists the required Python packages. You can install them using pip:

    ```bash
    pip install -r environment.txt
    ```

    This command will install Manim and any other libraries specified in the file.

The Manim animation is defined in the `merge_animation.py` file within the `Merge_sort` directory. You can run the animation using the following command from the root of your project directory:

```bash
manim -pqh Merge_sort/merge_animation.py MergeVector
```
