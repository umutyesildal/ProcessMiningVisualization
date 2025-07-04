Citation Suggestions for "Visualizing Event Type Distributions Over Time: Interactive Violin Charts for Process Mining Analysis"
1. Violin Plots and Distribution Visualization
Full Citation: Hintze, J. L., & Nelson, R. D. (1998). Violin plots: a box plot-density trace synergism. The American Statistician, 52(2), 181-184.
Link: DOI: 10.1080/00031305.1998.10480559
Summary: Introduces the violin plot as a novel graphical tool that combines the box plot with a density trace to reveal detailed distribution structure in the data
stat.cmu.edu
. This seminal paper demonstrates how violin plots provide insight into data distribution (e.g., showing multimodal patterns) that box plots alone might miss.
Suggested Use: Refer to this when explaining the choice of violin plots for visualizing event time distributions, to legitimize the method as an established statistical visualization technique in your methodology or introduction.
Full Citation: Weissgerber, T. L., Milic, N. M., Winham, S. J., & Garovic, V. D. (2015). Beyond bar and line graphs: Time for a new data presentation paradigm. PLOS Biology, 13(4), e1002128.
Link: DOI: 10.1371/journal.pbio.1002128
Summary: Argues that scientists should move away from simple bar/line graphs and instead display full data distributions (using scatterplots, boxplots, violin plots, etc.), because many different distributions can produce the same bar graph
journals.plos.org
. This work underlines the importance of depicting variability and distribution shape (clusters, outliers) rather than just summary statistics.
Suggested Use: Cite this in the introduction or related work to emphasize why showing the entire distribution (via violins) is crucial for accurate interpretation of event timing data, rather than aggregating into means that could conceal important process variations.
2. Process Mining Visual Analytics and Dashboards
Full Citation: Rehse, J.-R., Pufahl, L., Grohs, M., & Klein, L.-M. (2023). Process Mining Meets Visual Analytics: The Case of Conformance Checking. Proceedings of the 56th Hawaii International Conference on System Sciences (HICSS-56).
Link: AIS eLibrary: https://aisel.aisnet.org/hicss-56/os/business_process/4
Summary: Highlights the need for effective visualization in process mining, noting that even though process mining results can be complex, they must be presented in an approachable way for non-experts
aisel.aisnet.org
. The authors find that while some aspects of visualizing process data are well-supported, others (the “what” and “how” of visualization) remain under-explored
aisel.aisnet.org
, reinforcing the importance of interactive visual analytics.
Suggested Use: Use this as a reference in the related work section to support statements about the integration of visual analytics with process mining. It can also justify the novelty of your interactive dashboard by showing that presenting process mining results visually is an active research concern.
Full Citation: Fehrer, T., Moder, L., & Röglinger, M. (2025). An interactive approach for group-based event log exploration. Information Systems (Special Issue on Process Mining meets Visual Analytics), in press.
Link: DOI: 10.1016/j.is.2025.102575
Summary: Proposes the “Case Group Explorer,” an interactive visual analytics tool that helps analysts structure and explore complex event logs by grouping process cases and visualizing them
tobias-fehrer.de
. This approach demonstrates how user interaction and visual feedback can aid in identifying meaningful trace clusters and patterns in event data.
Suggested Use: Cite this when discussing the interactive dashboard or design of your visualization tool. It provides academic backing for using interactive grouping, sorting, and filtering in dashboards, and can be referenced in the methodology or tool implementation section to show you are building on state-of-the-art process mining analytics techniques.
3. Timeline-Based Event Visualization and Statistical Ordering
Full Citation: Monroe, M., Lan, R., Lee, H., Plaisant, C., & Shneiderman, B. (2013). Temporal Event Sequence Simplification. IEEE Transactions on Visualization and Computer Graphics, 19(12), 2227-2236.
Link: DOI: 10.1109/TVCG.2013.200
Summary: Presents EventFlow, a system that aligns and visualizes temporal event sequences for a cohort of entities (e.g. patients) by a reference point in time
cs.umd.edu
. By aligning records on key events (such as a first intervention) and plotting events before and after on a common timeline, this work shows how distributions of events over a normalized time axis can be compared and simplified for clarity.
Suggested Use: Reference this in the methodology when you describe aligning cases by a relative timeline (e.g., case start or milestone events). It supports the idea of viewing event occurrences in a time-normalized manner to compare patterns across cases.
Full Citation: Bodesinsky, P., Alsallakh, B., Gschwandtner, T., & Miksch, S. (2014). Visual Process Mining: Event Data Exploration and Analysis (IEEE VIS Workshop on Visual Analytics in Practice – Poster).
Link: PDF (Poster paper)
Summary: Demonstrates a prototype for interactive event log exploration that provides timeline-based overviews of event sequences (using visualizations like Dotted Charts for an “overview first” perspective) and allows dynamic reordering of cases based on various criteria
vis.cs.ucdavis.edu
vis.cs.ucdavis.edu
. By sorting process instances (e.g., by duration or frequency of a pattern), the tool helps analysts detect recurring patterns and deviations in event timing.
Suggested Use: Cite this when describing the visual sorting and arrangement features of your violin chart dashboard. It will strengthen the section where you discuss ordering events by statistics (median, quartiles) or the interface’s ability to sort cases/events, showing that similar approaches have been explored in process visualization research to enhance pattern discovery.
4. Applications in Real-World Domains (Traffic, Healthcare, Finance)
Full Citation: de Leoni, M., & Mannhardt, F. (2015). Road Traffic Fine Management Process (Event Log Dataset). Eindhoven University of Technology / 4TU ResearchData.
Link: DOI: 10.4121/uuid:270fd440-1057-4fb9-89a9-b699b47990f5
Summary: A real-life event log from an information system managing road traffic fines
data.4tu.nl
. This public dataset contains thousands of fines handling cases and is widely used to demonstrate process mining techniques on real administrative process data. It provides a rich example of timestamped events (from creation of fines to payment or closure) against which process visualization methods (like your violin charts) can be showcased.
Suggested Use: Mention this dataset in the case study section of your paper (especially if you use or reference the Road Traffic Fines log). It shows that your approach is evaluated on a credible, real-world process, and you can cite it when introducing the dataset or discussing results related to the traffic fines process.
Full Citation: Rojas, E., Munoz-Gama, J., Sepúlveda, M., & Capurro, D. (2016). Process mining in healthcare: A literature review. Journal of Biomedical Informatics, 61, 224–236.
Link: DOI: 10.1016/j.jbi.2016.04.007
Summary: Surveys 74 case studies of process mining applied in the healthcare domain, illustrating how process mining has been used to analyze clinical workflows, patient treatment processes, etc.
pmc.ncbi.nlm.nih.gov
. It highlights common challenges (like variability of medical processes) and the need for visual analytics to interpret complex care pathways.
Suggested Use: Use this source to justify any application of your visualization to healthcare logs or to claim that process mining (and by extension, visualizing event distributions) is valuable in healthcare. It can be cited in the introduction as evidence of interest in applying process mining to domains like healthcare, which your technique could support (e.g., visualizing patient journey event distributions).
Full Citation: van Dongen, B. (2012). BPI Challenge 2012 (Loan Application Event Log Dataset). Eindhoven University of Technology / 4TU ResearchData.
Link: DOI: 10.4121/uuid:3926db30-f712-4394-aebc-75976070e91f
Summary: The event log from the BPI 2012 Challenge, capturing a personal loan application process in a financial institution
web.tecnico.ulisboa.pt
. This dataset includes thousands of cases with events like application submission, offers, and approvals, providing a representative example of a finance domain process. It has been extensively analyzed in the process mining community and can serve to demonstrate the generalizability of visualization techniques.
Suggested Use: If your paper includes finance domain examples or mentions generalizability, cite this when discussing real-world evaluation. For instance, in a section about datasets or experiments, referencing this establishes that your approach could apply to financial processes (which often have many cases and events, benefiting from distribution visualization over time).
5. Interactive Visual Analytics Tools in Process Mining
Full Citation: Berti, A., van Zelst, S. J., & van der Aalst, W. M. P. (2019). Process Mining for Python (PM4Py): Bridging the gap between process- and data science. arXiv preprint arXiv:1905.06169.
Link: DOI: 10.48550/arXiv.1905.06169
Summary: Introduces PM4Py, an open-source Python library for process mining, aimed at integrating process mining algorithms with the data science ecosystem
arxiv.org
. The paper discusses limitations of existing tools (e.g., many are GUI-only or not easily extensible) and shows how PM4Py enables custom analytics and visualizations by leveraging Python’s libraries (pandas, Plotly, etc.).
Suggested Use: Cite this in the implementation section to justify your use of PM4Py for event log preprocessing. It establishes that PM4Py is a recognized framework in academia and helps explain how you were able to conveniently compute process mining metrics or prepare data for visualization.
Full Citation: Merkoureas, I., Kaouni, A., Theodoropoulou, G., Bousdekis, A., Voulodimos, A., & Miaoulis, G. (2023). Smyrida: A web application for process mining and interactive visualization. SoftwareX, 22, 101327.
Link: DOI: 10.1016/j.softx.2023.101327
Summary: Describes Smyrida, a modern process mining tool that offers an interactive web-based dashboard for process analysis. Smyrida is a modular software system with an intuitive UI and open APIs, making it easily extensible with new process mining techniques
pmc.ncbi.nlm.nih.gov
. It covers the full process mining pipeline (from log import to visual analytics) and exemplifies the trend of user-friendly, interactive process mining platforms.
Suggested Use: Use this as a reference when positioning your Plotly/Dash dashboard among existing tools. In the related work or conclusion, citing Smyrida shows that academia is moving toward interactive, web-based process mining solutions. It reinforces the contribution of your work in providing interactive visual analytics for process data, and you can mention it to highlight similarities or differences (e.g., your focus on violin charts for time distribution).

Citations

Violin Plots: A Box Plot-Density Trace Synergism

https://www.stat.cmu.edu/~rnugent/PCMI2016/papers/ViolinPlots.pdf

Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm | PLOS Biology

https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128
AIS Electronic Library (AISeL) - Hawaii International Conference on System Sciences 2023 (HICSS-56): Process Mining Meets Visual Analytics: The Case of Conformance Checking

https://aisel.aisnet.org/hicss-56/os/business_process/4/
AIS Electronic Library (AISeL) - Hawaii International Conference on System Sciences 2023 (HICSS-56): Process Mining Meets Visual Analytics: The Case of Conformance Checking

https://aisel.aisnet.org/hicss-56/os/business_process/4/

An Interactive Approach for Group-Based Event Log Exploration | Dr. Tobias Fehrer

https://tobias-fehrer.de/publication/interactive-log-exploration/

https://www.cs.umd.edu/~ben/Monroe2013Temporal.pdf
Visual Process Mining: Event Data Exploration and Analysis

https://vis.cs.ucdavis.edu/vis2014papers/VIS_Conference/vast/posters/bodesinsky.pdf
Visual Process Mining: Event Data Exploration and Analysis

https://vis.cs.ucdavis.edu/vis2014papers/VIS_Conference/vast/posters/bodesinsky.pdf

Road Traffic Fine Management Process (dataset)

https://data.4tu.nl/articles/dataset/Road_Traffic_Fine_Management_Process/12683249
Using Process Mining Techniques to Study Workflows in a Pre ...

https://pmc.ncbi.nlm.nih.gov/articles/PMC5977611/
https://web.tecnico.ulisboa.pt/diogo.ferreira/papers/lopes19survey.pdf

[1905.06169] Process Mining for Python (PM4Py): Bridging the Gap Between Process- and Data Science

https://arxiv.org/abs/1905.06169
Modelling and Predictive Monitoring of Business Processes under ...

https://pmc.ncbi.nlm.nih.gov/articles/PMC10422467/
All Sources

stat.cmu

journals.plos
aisel.aisnet

tobias-fehrer

cs.umd
vis.cs.ucdavis