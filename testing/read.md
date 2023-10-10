
* **k -- specific keyword**
* **s -- print**
* **v -- verbose**

**built in markers:**

* @pytest.mark.skip
* @pytest.mark.skipif(reason="skipping for this test")

**intentnally wanted to fail this test case because of funcationlity of this test case not ready. to ignore test failures make it as xfail marker.**

* @pytest.mark.xfail

**conftest**

'''
Conftest is mainly used for :
 lets say i have a fixtures in one test file.
 if i want use fixtures in all test files we can use to copy same fixture module on every test file . to avoid this issue we can use conftest
'''