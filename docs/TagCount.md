# TagCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**since_date** | **date** | The date from which we started counting the number of shifts with this tag. | 
**count** | **int** | The number of shifts with this tag on the scheduling start date. | 

## Example

```python
from pristime_sdk.models.tag_count import TagCount

# TODO update the JSON string below
json = "{}"
# create an instance of TagCount from a JSON string
tag_count_instance = TagCount.from_json(json)
# print the JSON string representation of the object
print(TagCount.to_json())

# convert the object into a dict
tag_count_dict = tag_count_instance.to_dict()
# create an instance of TagCount from a dict
tag_count_from_dict = TagCount.from_dict(tag_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


