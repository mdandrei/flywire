On Tue, Jun 2, 2026 at 5:17 PM FlyWire Codex <flywirecodex@gmail.com> wrote:
Dear Applicants,


We received a substantially larger number of applications than anticipated and are currently evaluating candidates for the final cohort.


In parallel, we invite you to participate in a one-week qualification challenge. 
This exercise is designed to evaluate your technical skills and research ability, 
as well as the ability to independently approach open-ended scientific problems. 
Please note that certain aspects of this assignment are intentionally left unspecified; 
you will be evaluated on your ability to make reasonable assumptions, and clearly communicate your approach. 


Final selection will be based on both prior qualifications and challenge performance.

The Qualification Challenge
The FlyWire Codex currently contains five connectomic datasets. 


Your task is to identify the largest neuronal circuit shared across at least three of these datasets.


For the purposes of this challenge, a circuit is defined as a directed induced subgraph. 
More formally, your objective is to identify a set of N neurons present in three of the five datasets such that the induced directed 
subgraphs formed by those neurons are mutually isomorphic (i.e. identical).


The underlying connectomes are weighted by synapse count; 
however, for simplicity edge weights should be ignored. 
All analyses should be performed on the corresponding unweighted directed graphs provided below as edge lists:


  • BANC edge list

  • FAFB edge list 

  • MANC edge list 

  • MAOL edge list 

  • MCNS edge list 

Deliverables
Solution File
Submit a CSV file containing:

Three columns, corresponding to the selected datasets.

N rows, corresponding to matched neurons across datasets.

Each row should contain the neuron identifiers that participate in the identified correspondence.


Optimization Objective
Maximize N, subject to the following constraints:

The induced directed connectivity structure must be identical across all three datasets.

If an edge exists between two matched neurons in one dataset, the corresponding edge must exist in the others.

Edge directionality must be preserved.

In other words, the correspondence must define mutually isomorphic directed induced subgraphs.





Research Component


Once you have identified the shared circuit, utilize the metadata available in Codex 
(cell types, neurotransmitters, annotations, literature references, etc.) to investigate its biological significance in one of the chosen datasets.


Select one of the three datasets and prepare a concise scientific summary (maximum one page) addressing the following:


Visualization of the identified circuit as a network graph.

Visualization of the constituent neurons using Codex 3D meshes.

Observations, interpretation or biological hypothesis regarding the circuit.

Relevant literature and citations.



The document may be formatted as a short report, research note, or scientific poster.


Submission by June 9, 11:59 PM EST:

To facilitate faster review, please refrain from submitting materials/questions by email. 

Use this submission form once you are ready to submit your solution (instructions inside).

If you encounter a substantial technical issue that prevents progress, submit a report using this form. 
Please submit one issue per form response - we will triage and email all participants if updates are necessary.

The use of AI tools is permitted and encouraged. However, submissions must reflect your own critical thinking and technical comprehension. 
Vague explanations, superficial AI-generated filler, or poorly understood methodologies will be evaluated unfavorably. 
We may prioritize methodological rigor and clarity over the size of the discovered circuit.


Tentative Timeline
June 1: Application deadline.

June 9: Qualification challenge submission deadline.

Mid June: Final decisions will be made and communicated to applicants.

Late June: Admitted candidates will be invited to a series of introductory Zoom meetings.

Early July: Project assignments will be finalized; teams formed where appropriate.

July - August: Primary research and project work period.

Late August: Participants will present their work.

Please note that this timeline is provisional. Specific dates and additional details will be communicated as they are finalized.


Best regards,

The FlyWire Team


 One attachment
  •  Scanned by Gmail



==================== June 8th update

Dear Applicants,

Thank you for your continued engagement with the qualification challenge. Following several inquiries, we have a few important updates and clarifications:

1. Extended Deadline: The submission deadline has been extended to June 12th, 11:59 PM EST.

2. Connectivity Requirement: The discovered isomorphic structures must be weakly connected.

3. Brain Region Clarification: There is no requirement that matched neurons come from the same brain regions across the 3 datasets, as this information was not provided in the data.

4. Resubmissions: If you have already submitted and would like to update your solution, simply update your GitHub repository. We will download all solutions from the provided links shortly after the deadline.

As a reminder, please submit your materials via the forms below:

  • Submission Form: https://docs.google.com/forms/d/1tkUWhqUz_SW_q9Wfo9DIpzi7Hp4MyUjrayKAvEDZYJ4
  • Inquiry Form: https://docs.google.com/forms/d/1oCHwF3ivVch_tGhOuVFVOWq0BDlMcngrZXtC2TVRCyQ

If you have any further questions, please use the inquiry form above.

Best regards,
The FlyWire Team
