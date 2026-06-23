import streamlit as st

from pipeline.intent import extract_intent
from pipeline.design import create_design
from pipeline.schema import generate_schema
from pipeline.validate import cross_validate
from pipeline.repair import repair
from runtime.simulator import simulate
from evaluation.metrics import update

st.title("AI App Builder ")

prompt = st.text_input("Describe your app:")

def handle_prompt(prompt):
    if len(prompt.split()) < 3:
        return None, "Please provide more details about your app"
    return prompt, None

if st.button("Generate App"):
    prompt, error = handle_prompt(prompt)

    if error:
        st.error(error)
    else:
        # STEP 1: Intent
        intent = extract_intent(prompt)
        st.subheader("Intent")
        st.json(intent)

        # STEP 2: Design
        design = create_design(intent)
        st.subheader("Design")
        st.json(design)

        # STEP 3: Schema
        schema = generate_schema(design)
        st.subheader("Schema")
        st.json(schema)

        # STEP 4: Validation
        errors = cross_validate(schema)
        st.subheader("Validation Errors")
        st.write(errors if errors else "No errors")

        repaired = False

        # STEP 5: Repair
        if errors:
            schema = repair(schema, errors)
            repaired = True
            st.subheader("Repaired Schema")
            st.json(schema)

        # STEP 6: Execution
        result = simulate(schema)
        st.subheader("Execution Result")
        st.json(result)

        # STEP 7: Metrics
        success = result["status"] == "success"
        metrics = update(success, repaired)

        st.subheader("Metrics")
        st.json(metrics)