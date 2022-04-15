# Python-SentiStrength

Python 3 Wrapper for SentiStrength.

**Note: This package has the SentiStrength JAR file built in to simplify access. However, the original author did not release the JAR free for commercial use. If you are using this for commercial purposes, please email the original author Dr. Mike Thelwall to buy the commercial license. More details about licensing at (http://sentistrength.wlv.ac.uk/).**

## Installation

You have to install `python >= 3.7` and `java JRE >= 1.8.0` first. Then, install this library with `pip`.

```sh
pip install pysenti
```

## Examples

Single string example:

```python
import pysenti

s = pysenti.get_senti('What a lovely day')
# SentiResult(positive=2, negative=-1, neutral=1)

s.scale()
# 1
s.is_positive()
# True
```

Multiple strings example:

If you have a list of strings, please use this function and don't call `get_senti` in a loop. This is because this function only opens one subprocess to process all strings in the list, whereas `get_senti` opens a new subprocess every time.

```python
import pysenti

pysenti.get_senti_list(['What a lovely day', 'I love cats'])
```

## Acknowledgments

* Big thanks to Dr. Mike Thelwall for access to SentiStrength.
