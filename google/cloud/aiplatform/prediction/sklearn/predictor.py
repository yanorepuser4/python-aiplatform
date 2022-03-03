# -*- coding: utf-8 -*-

# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import joblib
import numpy as np
from typing import Any

from google.cloud import storage
from google.cloud.aiplatform.prediction.predictor import Predictor


class SklearnPredictor(Predictor):
    """Default Predictor implementation for Sklearn models."""

    def __init__(self):
        return

    def load(self, gcs_artifacts_uri: str):
        """Loads the model artifact.

        Args:
            gcs_artifacts_uri (str):
                Required. The value of the environment variable AIP_STORAGE_URI.
        """
        gcs_client = storage.Client()
        with open("model.joblib", 'wb') as model_f:
            gcs_client.download_blob_to_file(
                f"{gcs_artifacts_uri}/model.joblib", model_f
            )
        self._model = joblib.load("model.joblib")

    def predict(self, instances: Any) -> Any:
        """Performs prediction.

        Args:
            instances (Any):
                Required. The instances to perform prediction.

        Returns:
            Prediction results.
        """
        instances = instances["instances"]
        inputs = np.asarray(instances)
        outputs = self._model.predict(inputs)
        return {"predictions": outputs.tolist()}
