from collections import defaultdict

N = int(input('Number of patient visits: '))

patients = set()
patient_details = []
total_treatment_time = defaultdict(int)
total_severity_score = defaultdict(int)

for n in range(N):
    patient_name = input('Patient Name: ')
    severity = int(input('Severity: '))
    treatment_time = int(input('Treatment Tine: '))

    patients.add(patient_name)
    patient_details.append((patient_name, severity, treatment_time))

    total_severity_score[patient_name] += severity
    total_treatment_time[patient_name] += treatment_time 
    

patient_details.sort()

key = lambda items : (-items[1], items[0])

max_severity = min(total_severity_score.items(), key)

# --- Optional: Display the Results ---
print("\n=== SUMMARY RESULTS ===")
print('Top Patient: ', max_severity[0], ' with score: ', max_severity[1])
print(patients, total_severity_score[patients])

for name in sorted(total_severity_score):
    total_sev = total_severity_score[name]
    total_time = total_treatment_time[name]
    print(name, total_time, total_sev)