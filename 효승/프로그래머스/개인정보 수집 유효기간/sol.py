def solution(today, terms, privacies):
    answer = []

    # 날짜를 년, 개월, 일수로 쪼갬(정수로 변환)
    today_year ,today_month, today_day = map(int, today.split('.'))

    # 개인정보 수집일자를 딕셔너리에 담음
    term_dict = {}
    for term in terms:
        term_name, term_month = term.split()
        term_dict[term_name] = int(term_month)

    # 각 개인정보를 순회하면서
    for i in range(len(privacies)):

        # 입력값들을 적절하게 쪼갬
        privacy_date, privacy_term = privacies[i].split()
        year, month, day = map(int, privacy_date.split('.'))
        
        # 계산을 편하게 하기위해 month에 1을 빼줌
        # 1월 -> 0, 12월 -> 11 이런식으로
        month -= 1

        # 약관으로 인해 더해줄 개월수를 가져옴
        add_month = term_dict[privacy_term]

        # 적절한 연산 진행
        year = year + (month + add_month) // 12
        month = (month + add_month) % 12 + 1

        # 조건문을 통해 각 상황마다 날짜를 비교
        if year < today_year:
            answer.append(i+1)

        elif year == today_year:

            if month < today_month:
                answer.append(i+1)

            elif month == today_month:
                if day <= today_day:
                    answer.append(i+1)

    return answer