Worked solo on Assignment 1 (as required)<br>
Used the repository of Chun-Chieh Tsai (cct367@nyu.edu; https://github.com/DishT)<br>
Link to my analysis: https://github.com/sgo230/PUI2017_cct367/blob/master/HW3_cct367/CibibikeReview_sgo230.md (also merged with his repo)
<br><br>

Worked solo on Assignment 2 to gather summary tables for various studies (see table below)<br><br>

Worked solo on Assignment 3. GitHub is having trouble displaying the .ipynb file, but it is correctly viewable in this generic Notebook viewer tool: https://nbviewer.jupyter.org/github/sgo230/PUI2017_sgo230/blob/master/HW4_sgo230/Assignment%203.ipynb. <br>
Please see my note about the sidedness of the test - went against Federica's skeleton notebook example and my best intuition in constructing the hypothesis tests in order to replicate the paper's results.<br><br>

Worked primarily solo on Assignment 4. Helped Davey with portions of the lat/long -> borough conversion. Offered other general assistance on that part to a few other CUSP students (not specific code but advice/guidelines). Same issue as above - notebook not rendering in GitHub. Viewable here: https://nbviewer.jupyter.org/github/sgo230/PUI2017_sgo230/blob/master/HW4_sgo230/Assignment%204.ipynb.
  
<b>Assignment 2 table:<b>


| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
ANCOVA	| 1, treatment vs. control group | categorical  | 1, insulin sensitivity index | categorical | | | 	Does Recombinant human growth hormone (rhGH) combined with rosiglitazone reduce the adverse effect of rhGH on insulin sensitivity? | Insulin sensitivity index for rhGH <= insulin sensitivity index for rhGH + rosiglitazone | 0.05 | [Recombinant Human Growth Hormone and Rosiglitazone for Abdominal Fat Accumulation in HIV-Infected Patients with Insulin Resistance: A Randomized, Double-Blind, Placebo-Controlled, Factorial Trial](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0061160#s2) |


| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Multiple regression	| 4, daily climate data, soil information, total available water, Palmer Drought Severity Index | quantitative, both continuous and discrete | 1, vegetative coverage | continuous | | | 	Is climate the primary driver for vegetative coverage in northern China? | Vegetation for areas with low drought indexes <> Vegetation for areas with high drought indexes | 0.05 | [Trend Patterns of Vegetative Coverage and Their Underlying Causes in the Deserts of Northwest China over 1982 – 2008](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0126044) |


| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Logistic regression	| 5, five marker combinations from flow cytometry measurements | categorical | 1, presence of acute myeloid leukemia (AML) | categorical (yes/no) | | | Is paper's machine learning model better at detecting AML using flow cytometry markers than existing models (EDF-MSE/LR-LASSO, Vilar, Biehl et al., Mean/LR-LASSO, and Mean/LDA)? | Existing models' AML detection rates >= the machine learning model's detection rate | 0.05 | [Leukemia Prediction Using Sparse Logistic Regression](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0072932) |

# FBB ANCOVA: the IV is not test or not test, but the rhGH vs rosiglitazone + rhGH, or all studies would have the same IV. 
# multiple regression:  what is this simbol <>? do you mean == ? 

# otherwise ok
