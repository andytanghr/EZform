# English version
form_dictionary_en = \
{
    'form': 'DL43', # Application for Renewal/Replacement/Change of a Texas DL or ID card
    'data': [
        # applicant information
        { 'x': 23, 'y': 20, 'w': 77, 'h': 3, 'value': last_name }, # last name
        { 'x': 23, 'y': 24, 'w': 74, 'h': 3, 'value': first_name }, # first name
        { 'x': 26, 'y': 29, 'w': 73, 'h': 3, 'value': middle_name }, # middle name
        { 'x': 17, 'y': 34, 'w': 82, 'h': 3, 'value': suffix }, # suffix
        { 'x': 26, 'y': 29, 'w': 73, 'h': 3, 'value': maiden_name }, # maiden name
        { 'x': 46, 'y': 44, 'w': 12, 'h': 3, 'value': birth_month }, # birth month (##)
        { 'x': 64, 'y': 44, 'w': 12, 'h': 3, 'value': birthday }, # birthday (##)
        { 'x': 81, 'y': 44, 'w': 12, 'h': 3, 'value': birth_year }, # birth year (####)
        { 'x': 12, 'y': 48, 'w': 20, 'h': 3, 'value': SSN1 }, # SSN1 (###)
        { 'x': 38, 'y': 48, 'w': 16, 'h': 3, 'value': SSN2 }, # SSN2 (##)
        { 'x': 60, 'y': 48, 'w': 27, 'h': 3, 'value': SSN3 }, # SSN3 (####)
        { 'x': 28, 'y': 55, 'w': 3, 'h': 3, 'value': male }, # sex male
        { 'x': 43, 'y': 55, 'w': 3, 'h': 3, 'value': female }, # sex female
        { 'x': 87, 'y': 55, 'w': 12, 'h': 3, 'value': weight }, # weight (lbs)
        { 'x': 24, 'y': 59, 'w': 25, 'h': 3, 'value': eye_color }, # eye color
        { 'x': 67, 'y': 59, 'w': 12, 'h': 3, 'value': height_ft }, # height (ft)
        { 'x': 87, 'y': 59, 'w': 12, 'h': 3, 'value': height_in }, # height (in)
        { 'x': 30, 'y': 64, 'w': 9, 'h': 3, 'value': race }, # race

        # contact information
        { 'x': 127, 'y': 20, 'w': 68, 'h': 3, 'value': home_phone }, # home phone
        { 'x': 128, 'y': 25, 'w': 66, 'h': 3, 'value': other_phone }, # other phone
        { 'x': 116, 'y': 30, 'w': 78, 'h': 3, 'value': email }, # email

        # address information
        { 'x': 139, 'y': 41, 'w': 56, 'h': 3, 'value': residential_address }, # residential address
        { 'x': 114, 'y': 46, 'w': 49, 'h': 3, 'value': residential_city }, # residential city
        { 'x': 175, 'y': 46, 'w': 20, 'h': 3, 'value': residential_state }, # residential state
        { 'x': 121, 'y': 52, 'w': 25, 'h': 3, 'value': residential_zip }, # residential ZIP
        { 'x': 161, 'y': 52, 'w': 34, 'h': 3, 'value': residential_county }, # residential county

        # if residential address is same as mailing, values in this group will be the same as the group immediately above
        { 'x': 133, 'y': 57, 'w': 62, 'h': 3, 'value': mailing_address}, # mailing address
        { 'x': 114, 'y': 62, 'w': 49, 'h': 3, 'value': mailing_city }, # mailing city
        { 'x': 175, 'y': 62, 'w': 20, 'h': 3, 'value': mailing state }, # mailing state
        { 'x': 121, 'y': 67, 'w': 25, 'h': 3, 'value': mailing_zip }, # mailing ZIP
        { 'x': 162, 'y': 67, 'w': 33, 'h': 3, 'value': mailing_county }, # mailing county

        # questions 1-10
        { 'x': 9.5, 'y': 83.5, 'w': 3, 'h': 3, 'value': q1yes }, # Q1 Y
        { 'x': 17.4, 'y': 83.5, 'w': 3, 'h': 3, 'value': q1no }, # Q1 N
        { 'x': 9.5, 'y': 87.4, 'w': 3, 'h': 3, 'value': q2yes }, # Q2 Y
        { 'x': 17.4, 'y': 87.4, 'w': 3, 'h': 3, 'value': q2no }, # Q2 N
        { 'x': 9.5, 'y': 101.5, 'w': 3, 'h': 3, 'value': q3yes }, # Q3 Y
        { 'x': 17.4, 'y': 101.5, 'w': 3, 'h': 3, 'value': q3no }, # Q3 N
        { 'x': 9.5, 'y': 105.4, 'w': 3, 'h': 3, 'value': q4yes }, # Q4 Y
        { 'x': 17.4, 'y': 105.4, 'w': 3, 'h': 3, 'value': q4no }, # Q4 N
        { 'x': 187 'y': 105, 'w': 8.5, 'h': 3, 'value': q4_amount }, # Q4 $ amount
        { 'x': 9.5, 'y': 109.2, 'w': 3, 'h': 3, 'value': q5yes }, # Q5 Y
        { 'x': 17.4, 'y': 109.2, 'w': 3, 'h': 3, 'value': q5no }, # Q5 N
        { 'x': 9.5, 'y': 113.1, 'w': 3, 'h': 3, 'value': q6yes }, # Q6 Y
        { 'x': 17.4, 'y': 113.1, 'w': 3, 'h': 3, 'value': q6no }, # Q6 N
        { 'x': 154 'y': 113, 'w': 8, 'h': 3, 'value': q6amount }, # Q6 # amount
        { 'x': 9.5, 'y': 120.2, 'w': 3, 'h': 3, 'value': q7yes }, # Q7 Y
        { 'x': 17.4, 'y': 120.2, 'w': 3, 'h': 3, 'value': qyno }, # Q7 N
        { 'x': 129 'y': 120, 'w': 8, 'h': 3, 'value': q7amount }, # Q7 $ amount
        { 'x': 9.5, 'y': 124.4, 'w': 3, 'h': 3, 'value': q8yes }, # Q8 Y
        { 'x': 17.4, 'y': 124.4, 'w': 3, 'h': 3, 'value': q8no }, # Q8 N
        { 'x': 148 'y': 123, 'w': 51, 'h': 3, 'value': q8text }, # Q8 text
        { 'x': 9.5, 'y': 131.8, 'w': 3, 'h': 3, 'value': q9yes }, # Q9 Y
        { 'x': 17.4, 'y': 131.8, 'w': 3, 'h': 3, 'value': q9no }, # Q9 N
        { 'x': 9.5, 'y': 143.4, 'w': 3, 'h': 3, 'value': q10yes }, # Q10 Y
        { 'x': 17.4, 'y': 143.4, 'w': 3, 'h': 3, 'value': q10no }, # Q10 N
        { 'x': 36, 'y': 147, 'w': 43, 'h': 3, 'value': q10a_emergency_name }, # Q10a emergency name
        { 'x': 104, 'y': 147, 'w': 35, 'h': 3, 'value': q10a_emergency_phone }, # Q10a emergency phone number 
        { 'x': 150, 'y': 147, 'w': 48, 'h': 3, 'value': q10a_emergency_address }, # Q10a emergency address
        { 'x': 36, 'y': 151, 'w': 43, 'h': 3, 'value': q10b_emergency_name }, # Q10b emergency name
        { 'x': 104, 'y': 151, 'w': 35, 'h': 3, 'value': q10b_emergency_phone }, # Q10b emergency phone number 
        { 'x': 150, 'y': 151, 'w': 48, 'h': 3, 'value': q10b_emergency_address }, # Q10b emergency address

        # questions 11-17
        { 'x': 9.5, 'y': 160.7, 'w': 3, 'h': 3, 'value': q11yes }, # Q11 Y
        { 'x': 17.4, 'y': 146, 'w': 3, 'h': 3, 'value': q11no }, # Q11 N
        { 'x': 58, 'y': 146, 'w': 3, 'h': 3, 'value': q11improved }, # Q11 improved
        { 'x': 80, 'y': 146, 'w': 3, 'h': 3, 'value': q11deteriorated }, # Q11 deteriorated
        { 'x': 9.5, 'y': 146, 'w': 3, 'h': 3, 'value': q12yes }, # Q12 Y
        { 'x': 17.4, 'y': 146, 'w': 3, 'h': 3, 'value': q12no }, # Q12 N
        { 'x': ///, 'y': 146, 'w': 174, 'h': 3, 'value': q12text }, # Q12 text
        { 'x': 9.5, 'y': 146, 'w': 3, 'h': 3, 'value': q13yes }, # Q13 Y
        { 'x': 17.4, 'y': 146, 'w': 3, 'h': 3, 'value': q13no }, # Q13 N
        { 'x': 9.5, 'y': 146, 'w': 3, 'h': 3, 'value': q14yes }, # Q14 Y
        { 'x': 17.4, 'y': 146, 'w': 3, 'h': 3, 'value': q14no }, # Q14 N
        { 'x': 9.5, 'y': 146, 'w': 3, 'h': 3, 'value': q15yes }, # Q15 Y
        { 'x': 17.4, 'y': 146, 'w': 3, 'h': 3, 'value': q15no }, # Q15 N
        { 'x': 9.5, 'y': 146, 'w': 3, 'h': 3, 'value': q16yes }, # Q16 Y
        { 'x': 17.4, 'y': 146, 'w': 3, 'h': 3, 'value': q16no }, # Q16 N
        { 'x': ////, 'y': 146, 'w': 163, 'h': 3, 'value': q16text }, # Q16 text
        { 'x': 9.5, 'y': 146, 'w': 3, 'h': 3, 'value': q17yes }, # Q17 Y
        { 'x': 17.4, 'y': 146, 'w': 3, 'h': 3, 'value': q17no }, # Q17 N

        # affirmation/signature question about housing type (house, apartment, motel, shelter)
        { 'x': 42, 'y': 248, 'w': 3, 'h': 3, 'value': house }, # house
        { 'x': 74, 'y': 248, 'w': 3, 'h': 3, 'value': apartment }, # apartment
        { 'x': 92, 'y': 248, 'w': 3, 'h': 3, 'value': motel }, # motel
        { 'x': 105, 'y': 248, 'w': 3, 'h': 3, 'value': shelter }, # shelter

    ]
}


# Spanish version
form_dictionary_es = \ 
{
    'form': 'DL43', # Application for Renewal/Replacement/Change of a Texas DL or ID card
    'data': [
        # applicant information
        { 'x': 19, 'y': 21, 'w': 80, 'h': 3, 'value': last_name }, # last name
        { 'x': 49, 'y': 22, 'w': 70, 'h': 3, 'value': first_name }, # first name
        { 'x': 32, 'y': 29, 'w': 67, 'h': 3, 'value': middle_name }, # middle name
        { 'x': 15, 'y': 34, 'w': 83, 'h': 3, 'value': suffix }, # suffix
        { 'x': 37, 'y': 38, 'w': 62, 'h': 3, 'value': maiden_name }, # maiden name
        { 'x': 54, 'y': 43, 'w': 12, 'h': 3, 'value': birth_month + ' - ' }, # birth month (##)
        { 'x': 66, 'y': 43, 'w': 12, 'h': 3, 'value': birthday + ' - ' }, # birthday (##)
        { 'x': 78, 'y': 43, 'w': 12, 'h': 3, 'value': birth_year }, # birth year (####)
        { 'x': 45, 'y': 47, 'w': 13, 'h': 3, 'value': SSN1 }, # SSN1 (###)
        { 'x': 62, 'y': 47, 'w': 10, 'h': 3, 'value': SSN2 }, # SSN2 (##)
        { 'x': 77, 'y': 47, 'w': 16, 'h': 3, 'value': SSN3 }, # SSN3 (####)
        { 'x': 30, 'y': 47, 'w': 3, 'h': 3, 'value': male }, # sex male
        { 'x': 48, 'y': 52, 'w': 3, 'h': 3, 'value': female }, # sex female
        { 'x': 86, 'y': 50, 'w': 12, 'h': 3, 'value': weight }, # weight (lbs)
        { 'x': 34, 'y': 56, 'w': 20, 'h': 3, 'value': eye_color }, # eye color
        { 'x': 77, 'y': 56, 'w': 7, 'h': 3, 'value': height_ft }, # height (ft)
        { 'x': 92, 'y': 56, 'w': 6, 'h': 3, 'value': height_in }, # height (in)
        { 'x': 21, 'y': 60, 'w': 9, 'h': 3, 'value': race }, # race

        # contact information
        { 'x': 135, 'y': 21, 'w': 61, 'h': 3, 'value': home_phone }, # home phone
        { 'x': 136, 'y': 25, 'w': 59, 'h': 3, 'value': other_phone }, # other phone
        { 'x': 135, 'y': 29, 'w': 61, 'h': 3, 'value': email }, # email

        # address information
        { 'x': 139, 'y': 38, 'w': 57, 'h': 3, 'value': residential_address }, # residential address
        { 'x': 114, 'y': 43, 'w': 42, 'h': 3, 'value': residential_city }, # residential city
        { 'x': 170, 'y': 43, 'w': 25, 'h': 3, 'value': residential_state }, # residential state
        { 'x': 125, 'y': 47, 'w': 23, 'h': 3, 'value': residential_zip }, # residential ZIP
        { 'x': 165, 'y': 47, 'w': 30, 'h': 3, 'value': residential_county }, # residential county

        # if residential address is same as mailing, values in this group will be the same as the group immediately above
        { 'x': 102, 'y': 56, 'w': 93, 'h': 3, 'value': mailing_address}, # mailing address
        { 'x': 114, 'y': 60, 'w': 40, 'h': 3, 'value': mailing_city }, # mailing city
        { 'x': 168, 'y': 60, 'w': 27, 'h': 3, 'value': mailing state }, # mailing state
        { 'x': 125, 'y': 64, 'w': 23, 'h': 3, 'value': mailing_zip }, # mailing ZIP
        { 'x': 165, 'y': 64, 'w': 30 , 'h': 3, 'value': mailing_county }, # mailing county

        # questions 1-10
        { 'x': 9.6, 'y': 80, 'w': 3, 'h': 3, 'value': q1yes }, # Q1 Y
        { 'x': 17.4, 'y': 80, 'w': 3, 'h': 3, 'value': q1no }, # Q1 N
        { 'x': 9.6, 'y': 83, 'w': 3, 'h': 3, 'value': q2yes }, # Q2 Y
        { 'x': 17.4, 'y': 83, 'w': 3, 'h': 3, 'value': q2no }, # Q2 N
        { 'x': 9.6, 'y': 97, 'w': 3, 'h': 3, 'value': q3yes }, # Q3 Y
        { 'x': 17.4, 'y': 97, 'w': 3, 'h': 3, 'value': q3no }, # Q3 N
        { 'x': 9.6, 'y': 101, 'w': 3, 'h': 3, 'value': q4yes }, # Q4 Y
        { 'x': 17.4, 'y': 101, 'w': 3, 'h': 3, 'value': q4no }, # Q4 N
        { 'x': 41, 'y': 104, 'w': 8, 'h': 3, 'value': q4_amount }, # Q4 $ amount
        { 'x': 9.6, 'y': 108, 'w': 3, 'h': 3, 'value': q5yes }, # Q5 Y
        { 'x': 17.4, 'y': 108, 'w': 3, 'h': 3, 'value': q5no }, # Q5 N
        { 'x': 9.6, 'y': 112, 'w': 3, 'h': 3, 'value': q6yes }, # Q6 Y
        { 'x': 17.4, 'y': 112, 'w': 3, 'h': 3, 'value': q6no }, # Q6 N
        { 'x': 169, 'y': 112, 'w': 8, 'h': 3, 'value': q6amount }, # Q6 $ amount
        { 'x': 9.6, 'y': 119, 'w': 3, 'h': 3, 'value': q7yes }, # Q7 Y
        { 'x': 17.4, 'y': 119, 'w': 3, 'h': 3, 'value': qyno }, # Q7 N
        { 'x': 155, 'y': 119, 'w': 8, 'h': 3, 'value': q7amount }, # Q7 $ amount
        { 'x': 9.6, 'y': 123, 'w': 3, 'h': 3, 'value': q8yes }, # Q8 Y
        { 'x': 17.4, 'y': 123, 'w': 3, 'h': 3, 'value': q8no }, # Q8 N
        { 'x': 24, 'y': 127, 'w': 42, 'h': 3, 'value': q8text }, # Q8 text
        { 'x': 9.6, 'y': 131, 'w': 3, 'h': 3, 'value': q9yes }, # Q9 Y
        { 'x': 17.4, 'y': 131, 'w': 3, 'h': 3, 'value': q9no }, # Q9 N
        { 'x': 9.6, 'y': 145, 'w': 3, 'h': 3, 'value': q10yes }, # Q10 Y
        { 'x': 17.4, 'y': 145, 'w': 3, 'h': 3, 'value': q10no }, # Q10 N
        { 'x': 39, 'y': 148, 'w': 40, 'h': 3, 'value': q10a_emergency_name }, # Q10a emergency name
        { 'x': 102, 'y': 148, 'w': 35, 'h': 3, 'value': q10a_emergency_phone }, # Q10a emergency phone number 
        { 'x': 150, 'y': 148, 'w': 48, 'h': 3, 'value': q10a_emergency_address }, # Q10a emergency address
        { 'x': 39, 'y': 153, 'w': 40, 'h': 3, 'value': q10b_emergency_name }, # Q10b emergency name
        { 'x': 102, 'y': 153, 'w': 35, 'h': 3, 'value': q10b_emergency_phone }, # Q10b emergency phone number 
        { 'x': 150, 'y': 153, 'w': 48, 'h': 3, 'value': q10b_emergency_address }, # Q10b emergency address

        # questions 11-17
        { 'x': 9.6, 'y': 163, 'w': 3, 'h': 3, 'value': q11yes }, # Q11 Y
        { 'x': 17.4, 'y': 163, 'w': 3, 'h': 3, 'value': q11no }, # Q11 N
        { 'x': 68, 'y': 184, 'w': 3, 'h': 3, 'value': q11improved }, # Q11 improved
        { 'x': 91, 'y': 184, 'w': 3, 'h': 3, 'value': q11deteriorated }, # Q11 deteriorated
        { 'x': 9.6, 'y': 188, 'w': 3, 'h': 3, 'value': q12yes }, # Q12 Y
        { 'x': 17.4, 'y': 188, 'w': 3, 'h': 3, 'value': q12no }, # Q12 N
        { 'x': 50, 'y': 191, 'w': 148, 'h': 3, 'value': q12text }, # Q12 text
        { 'x': 9.6, 'y': 195, 'w': 3, 'h': 3, 'value': q13yes }, # Q13 Y
        { 'x': 17.4, 'y': 195, 'w': 3, 'h': 3, 'value': q13no }, # Q13 N
        { 'x': 9.6, 'y': 199, 'w': 3, 'h': 3, 'value': q14yes }, # Q14 Y
        { 'x': 17.4, 'y': 199, 'w': 3, 'h': 3, 'value': q14no }, # Q14 N
        { 'x': 9.6, 'y': 146, 'w': 3, 'h': 3, 'value': q15yes }, # Q15 Y
        { 'x': 17.4, 'y': 203, 'w': 3, 'h': 3, 'value': q15no }, # Q15 N
        { 'x': 9.6, 'y': 203, 'w': 3, 'h': 3, 'value': q16yes }, # Q16 Y
        { 'x': 17.4, 'y': 210, 'w': 3, 'h': 3, 'value': q16no }, # Q16 N
        { 'x': 13, 'y': 210, 'w': 161, 'h': 3, 'value': q16text }, # Q16 text
        { 'x': 9.6, 'y': 216, 'w': 3, 'h': 3, 'value': q17yes }, # Q17 Y
        { 'x': 17.4, 'y': 216, 'w': 3, 'h': 3, 'value': q17no }, # Q17 N

        # affirmation/signature question about housing type (house, apartment, motel, shelter)
        { 'x': 76, 'y': 249, 'w': 3, 'h': 3, 'value': house }, # house
        { 'x': 100, 'y': 249, 'w': 3, 'h': 3, 'value': apartment }, # apartment
        { 'x': 121, 'y': 249, 'w': 3, 'h': 3, 'value': motel }, # motel
        { 'x': 132, 'y': 249, 'w': 3, 'h': 3, 'value': shelter }, # shelter

    ]
}