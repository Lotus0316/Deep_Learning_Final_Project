# Deep_Learning_Final_Project
## File tree
```markdown DEEP_LEARNING_FINAL_PROJECT
DEEP_LEARNING_FINAL_PROJECT
├── cleaned_data/
    ├── flited_data/
    ├── graph_data/
    └── splited_data/
├── code/
├── Picture/
├── yelp_dataset/
    └── yalp_academic_dataset_xxx.json
├── yelp_photos/photo_file
    ├── photos/
    └── photos.json
├── .gitignore
├── Proposal_pre_for_team_16.pdf
└── README.md
```
## Required library
- **requirements.txt:** All libraries required for this project.

## Workflow and Code Details

1. **`filter.ipynb`** and **`train-test-split.ipynb`**
   - Perform data filtering and splitting.
   - Output: Training and test sets in JSON files (`*.json`).
2. `Node_data.ipynb`
   - Select all nodes' data
3. `Edge_n_weight.ipynb`
   - Create edge data
   - Calculate weight
4. **`ndata.ipynb`**
   - Outputs processed node features in NumPy files (`*.npy`).
5. **`graph-construction.ipynb`**
   - Takes the two TXT files, node features, and the predicted tip ratings.
   - Outputs the binary file of the graph (`*.bin`).
6. **`a-gnn.ipynb`**
   - Takes the graph (`*.bin`) as input and outputs the predictions as `*.npy`.
7. **`fig3b.ipynb`**
   - Analyzes the output and plots Figure 3b.
8. **`all_models.ipynb`**
   - Takes as input:
     - Predictions of the GNN (`*.npy`).
     - `node_type_ID.txt`
     - The split `*.json` (training and test sets).
   - Prints evaluation metrics of the models.
   - Outputs predictions as `*.npy`.
9. **`Geographical Recommend.py`**
   - Sorts the nearest stores around a given location and recommends the stores based on a pre-ranked matrix for each user.
   - Example
     - one user has a row of 1,434 elements where each element represents the weight of how likely the user will visit that store.
     - Stores are selected based on the `dist` function.
     - Filtered stores are reranked based on weights using the function `recall at 20`.

