Hi, I'm Geraint. I'm in the final year of my PhD and am working with Professor Paul Harper and Dr Vincent Knight. Currently I'm working on the evaluation of new Stay Well Plans in the Newport area, and modelling around its impact on healthcare workforce.

---

I am working with Aneurin Bevan University Health Board, that serves the Gwent. This is made up from 5 very different counties. Very varied levels of deprivation, population density, and healthcare needs. In fact both the most and least deprived areas in Wales lie within these borders.

Stay Well Plans are a new initiative offered to some older people living in the area.
These consist of a home visit where a care facilitator can inspect the home, talk with the patient, and give tailored adivce and guidance on a number of lifestyle factors. These include home safety, family and social interactions, advice on nutrition and personal hygine, and guidance on appropriate access to healthcare services.

Patients are selected to be offered plans by their GPs, this could be based on age, personal needs, or more popularly by the use of a risk stratification tool that identifies those patients most at risk of becoming frequent users of the healthcare system.

The initiative was trialled in Newport, and it is this cohort of individuals who are analysed in this work. Using modelling we can then look at the effect of rolling out the plans across all five counties in Gwent.

---

The plans were delivered gradually accross three years. Some patients who were offered did not accept a plan, and more recently some were referred to a plan from Frailty services, represented here in orange. By the end of the observation period, roughly 8% of patients were offered a plan, and about 80% of these accepted.

---

For the models I partitioned the population into three groups: Those that were offered and accepted plans, those that received a plan from Frailty services, and those who did not receive a plan. The size of these groups are dependant on three parameters
+ p_o the probability of beign offered
+ p_a the probability of accepting
+ p_f the probability of being referred by Frailty.

These parameters would be different for each county. The probability of being offered a plan depends on the management, which would be varied as model scenarios. The probability of accepting a plan can be predicted from deprivation levels.

---

Working closely with healthcare managers this map of the healthcare system used by older people was drawn and is the focus of the analysis. We are interested the the affect of the plans on emergency secondary care service, Frailty services, and community care services.

This network is being modelled as a queueing network, and the analysis is being carried out using discrete event simulation. Some things, the greyed out areas, though important to consider, are omitted from the model. The effect on the demand and required staffing levels at the four Frailty specialities, and emergency admission ward at the three hospitals are the focus.

---

A lot of data analysis has been carried out so far and we have a number of findings that may be explained by two main conclusions: Preventative measures are encouraged and are having some positive effects, however those receiving the plans are inherantly frailer than the rest of the population.

We are seeing significantly more patients having lower attendancec after a SWP, though the overall number of attendances for SWP patients has increased.

We are seeing shorter durations of community care packages, however longer lengths of stays at hospitals.

Admissions for Urology has decreased, which may be due to the personal hygine guidance of the plans. Though they are more likely to attend for care of the elderly services.

SWP patients are more likely to be referred to community care services after an emergency admission. Though they are more likely to be admitted to hospital after A&E (therefore we think they are attending for more severe ailments).

They are also more likely to require Rapid Medical Frailty services.

Simulations on the rollout are being run to see if these effects are significant as the numbers of patients increase.

---

Finally right now we are focussing on mapping changes in demand at each facility to changes in workforce needs. We are especially looking at numbers of beds and staffing at hospital wards, reactive frailty services, and community care services. My crude belief at the moment is that there will be a significant effect on demand and staffing requirements for Frailty services.

Thank you.