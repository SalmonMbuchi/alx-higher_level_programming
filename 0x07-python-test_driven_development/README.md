# Test Driven Development(TDD)



“Test-driven development” refers to a style of programming in which three activities are tightly interwoven: coding, testing (in the form of writing unit tests) and design (in the form of refactoring).

It can be succinctly described by the following set of rules:

    1. write a “single” unit test describing an aspect of the program
    2. run the test, which should fail because the program lacks that feature
    3. write “just enough” code, the simplest possible, to make the test pass
    4. “refactor” the code until it conforms to the simplicity criteria
    5. repeat, “accumulating” unit tests over time

## Expected Benefits

Some of the benefits include:
    1. many teams report significant reductions in defect rates, at the cost of a moderate increase in initial development effort
    2. the same teams tend to report that these overheads are more than offset by a reduction in effort in projects’ final phases
    3. although empirical research has so far failed to confirm this, veteran practitioners report that TDD leads to improved design qualities in the code, and more generally a higher degree of “internal” or technical quality, for instance improving the metrics of cohesion and coupling

## Common Pitfalls

Typical individual mistakes include:

    1. forgetting to run tests frequently
    2. writing too many tests at once
    3. writing tests that are too large or coarse-grained
    4. writing overly trivial tests, for instance omitting assertions
    5. writing tests for trivial code, for instance accessors

Typical team pitfalls include:

    1. partial adoption – only a few developers on the team use TDD
    2. poor maintenance of the test suite – most commonly leading to a test suite with a prohibitively long running time
    3. abandoned test suite (i.e. seldom or never run) – sometimes as a result of poor maintenance, sometimes as a result of team turnover


