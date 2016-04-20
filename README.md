# upipe

## Example
```python
>>> "adf 1 1 3 4" | Reverse | Filter(str.isdigit) | Map(int) | Map(lambda x: x + 1)  | Set
{2, 4, 5}
```