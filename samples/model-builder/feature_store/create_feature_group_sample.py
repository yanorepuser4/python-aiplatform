# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#  [START aiplatform_sdk_create_feature_group_sample]

from google.cloud import aiplatform
from vertexai.resources.preview import feature_store
from typing import List


def create_feature_group_sample(
    project: str,
    location: str,
    feature_group_id: str,
    bq_table_uri: str,
    entity_id_columns: List[str],
):
    aiplatform.init(project=project, location=location)
    fg = feature_store.FeatureGroup.create(
        name=feature_group_id,
        source=feature_store.utils.FeatureGroupBigQuerySource(
            uri=bq_table_uri, entity_id_columns=entity_id_columns
        ),
    )
    return fg


#  [END aiplatform_sdk_create_feature_group_sample]
