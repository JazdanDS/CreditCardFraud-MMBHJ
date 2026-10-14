from collections import Counter

from imblearn.over_sampling import SMOTE

def apply_smote(X_train, y_train):
    smote = SMOTE(random_state=42) #lägg till sampling strategy här och testa olika nivåer

    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    print("Before SMOTE:", Counter(y_train))
    print("After SMOTE:", Counter(y_resampled))

    return X_resampled, y_resampled

