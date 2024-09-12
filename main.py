import streamlit as st
import requests
import json

def generate_response(prompt):
    url = "https://data.kreat.space/chatgpt_answer"
    headers = {"Content-Type": "application/json"}
    data = {"question": prompt}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def main():
    st.title("Comprehensive Problem Analysis Diagnosis")

    problem_statement = st.text_area("Enter your problem statement:")
    
    if st.button("Generate Analysis"):
        if problem_statement:
            sections = [
                ("1. Problem Definition and Context", [
                    "1.1 Core Problem Statement",
                    "1.2 Historical Context",
                    "1.3 Current Landscape",
                    "1.4 Future Projections"
                ]),
                ("2. Stakeholder Analysis", [
                    "2.1 Key Stakeholders",
                    "2.2 Stakeholder Relationships",
                    "2.3 Impact on Stakeholders"
                ]),
                ("3. Impact Assessment", [
                    "3.1 Environmental Impact",
                    "3.2 Social Impact",
                    "3.3 Economic Impact",
                    "3.4 Technological Impact"
                ]),
                ("4. Root Cause Analysis", [
                    "4.1 Five Whys Technique",
                    "4.2 Contributing Factors"
                ]),
                ("5. Systems Thinking", [
                    "5.1 System Components",
                    "5.2 Interactions and Relationships",
                    "5.3 System Boundaries"
                ]),
                ("6. Quantitative Analysis", [
                    "6.1 Key Metrics",
                    "6.2 Data Sources",
                    "6.3 Trends and Patterns"
                ]),
                ("7. Regulatory and Policy Landscape", [
                    "7.1 Current Regulations",
                    "7.2 Regulatory Gaps"
                ]),
                ("8. Technological Context", [
                    "8.1 Current Technologies",
                    "8.2 Emerging Technologies"
                ]),
                ("9. Complexity Assessment", [
                    "9.1 Interconnected Factors",
                    "9.2 Predictability",
                    "9.3 Dynamic Nature"
                ]),
                ("10. Function Analysis", [
                    "10.1 Useful Functions",
                    "10.2 Harmful Functions"
                ]),
                ("11. Comparative Analysis", [
                    "11.1 Similar Problems",
                    "11.2 Benchmarking"
                ]),
                ("12. Ethical Considerations", [
                    "12.1 Moral Implications",
                    "12.2 Conflicting Values"
                ]),
                ("13. Resource Analysis", [
                    "13.1 Required Resources",
                    "13.2 Resource Constraints"
                ]),
                ("14. Risk Assessment", [
                    "14.1 Current Risks",
                    "14.2 Future Risks"
                ]),
                ("15. Conclusion", [
                    "15.1 Summary of Key Findings",
                    "15.2 Implications",
                    "15.3 Next Steps"
                ])
            ]

            for main_section, subsections in sections:
                st.header(main_section)
                for subsection in subsections:
                    # st.subheader(subsection)
                    prompt = f"Given the problem statement: '{problem_statement}', provide an analysis for the section '{subsection}' of the Comprehensive Problem Analysis Framework."
                    response = generate_response(prompt)
                    st.write(response)
                st.markdown("---")
        else:
            st.warning("Please enter a problem statement.")

if __name__ == "__main__":
    main()
