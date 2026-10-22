from collections import Counter

from imblearn.over_sampling import SMOTE

def apply_smote(X_train, y_train, sampling_strategy=1.0, k_neighbors=5):
    smote = SMOTE(
        sampling_strategy=sampling_strategy,
        k_neighbors=k_neighbors,
        random_state=42
    )

    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    print("Before SMOTE:", Counter(y_train))
    print("After SMOTE:", Counter(y_resampled))
    print("k_neighbors:", k_neighbors)

    return X_resampled, y_resampled

