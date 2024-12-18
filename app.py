import streamlit as st
import os
from PIL import Image

# App Title
st.title("MNIST Dimensionality Reduction Report")

# Visualization Directory
output_dir = "visualizations"

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Introduction", "Visualizations", "Trade-Off Analysis", "Image Reconstruction", "Summary"])

# Section 1: Introduction
if page == "Introduction":
    st.header("Introduction")
    st.write("""
Dimensionality reduction techniques such as **PCA** (Principal Component Analysis) and **t-SNE** help simplify high-dimensional datasets like MNIST, which contains images of handwritten digits.

In this report, we explore:
1. **PCA** for variance analysis and reconstruction.
2. **t-SNE** for non-linear visualization.
3. The trade-off between **information loss** and **computational efficiency**.
4. The effectiveness of these methods for **image data analysis**.
""")
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png", caption="Sample MNIST Digits", use_container_width=True)
    st.write("Let's dive into the visualizations and analysis!")

# Section 2: Visualizations
elif page == "Visualizations":
    st.header("Visualizing High-Dimensional Data")

    # PCA Visualization
    st.subheader("PCA Visualization")
    pca_image_path = os.path.join(output_dir, "pca_visualization.png")
    if os.path.exists(pca_image_path):
        st.image(Image.open(pca_image_path), caption="PCA: Reduced to 2D", use_container_width=True)
    else:
        st.warning("PCA visualization image not found!")

    st.write("""
PCA reduces data to its principal components, retaining the most significant patterns. 
Here, the MNIST data is visualized in 2D using PCA.
""")

    # t-SNE Visualization
    st.subheader("t-SNE Visualization")
    tsne_image_path = os.path.join(output_dir, "tsne_visualization.png")
    if os.path.exists(tsne_image_path):
        st.image(Image.open(tsne_image_path), caption="t-SNE: Reduced to 2D", use_container_width=True)
    else:
        st.warning("t-SNE visualization image not found!")

    st.write("""
t-SNE captures non-linear relationships in the data, making it particularly effective for visualizing local clusters. 
Here, distinct groups of digits can be observed.
""")

# Section 3: Trade-Off Analysis
elif page == "Trade-Off Analysis":
    st.header("Trade-Off: Information Loss vs Efficiency")
    st.write("""
Dimensionality reduction improves computational efficiency but may result in information loss. Analyzing **explained variance** helps quantify this trade-off.
""")

    # Variance Analysis Plot
    st.subheader("Cumulative Explained Variance")
    variance_plot_path = os.path.join(output_dir, "variance_plot.png")
    if os.path.exists(variance_plot_path):
        st.image(Image.open(variance_plot_path), caption="Explained Variance Across PCA Components", use_container_width=True)
    else:
        st.warning("Variance plot image not found!")

    # Variance Analysis Summary
    variance_text_path = os.path.join(output_dir, "variance_analysis.txt")
    if os.path.exists(variance_text_path):
        st.subheader("Variance Analysis Summary")
        with open(variance_text_path, "r") as f:
            variance_content = f.read()
        st.text(variance_content)
    else:
        st.warning("Variance analysis text not found!")

    st.write("""
From the analysis:
- **Fewer components** retain less variance but reduce computational cost.
- **More components** preserve more information but increase processing time.
""")

# Section 4: Image Reconstruction
elif page == "Image Reconstruction":
    st.header("Original vs Reconstructed Images")

    st.write("""
PCA can also be used to **reconstruct images** by retaining only the most significant components. Below, we compare the original MNIST digits with their reconstructions after applying PCA with 100 components.
""")

    # Original vs Reconstructed Images
    reconstruction_image_path = os.path.join(output_dir, "reconstruction_comparison.png")
    if os.path.exists(reconstruction_image_path):
        st.image(Image.open(reconstruction_image_path), caption="Original (Top) vs Reconstructed (Bottom)", use_container_width=True)
    else:
        st.warning("Reconstruction comparison image not found!")

    st.write("""
Although the reconstructed images retain the general structure of the digits, some fine details are lost due to dimensionality reduction.
""")

# Section 5: Summary
elif page == "Summary":
    st.header("Summary")
    st.write("""
### Key Takeaways:
1. **PCA** effectively reduces dimensionality while retaining most of the variance, making it suitable for linear patterns and reconstructions.
2. **t-SNE** preserves local relationships, providing clearer visualizations of clusters in complex, non-linear data.
3. **Trade-Off**:
   - Reducing dimensions improves computational efficiency.
   - However, fewer dimensions may lead to some **information loss**.
4. Dimensionality reduction is a powerful tool for analyzing and visualizing high-dimensional image data.

Overall, these techniques simplify data without significantly compromising its structure, enabling better insights and efficiency.
""")

    st.markdown("---")
    st.write("Thank you for exploring this analysis! 🚀")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Created with Streamlit | MNIST Data Analysis")
