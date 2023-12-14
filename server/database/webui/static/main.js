async function naming() {
    const userPrompt = document.getElementById('input').value;
    if (!userPrompt.trim()) {
        return;
    }
    document.querySelector('#status').style.backgroundColor = '#ee7e00';
    document.querySelector('#status').innerText = `닉네임 생성중...`;
    const language = `ko`;
    const response = await fetch(`/api/generate/${language}/name`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(
            {
                "prompt": userPrompt,
            }
        ),
    });
    const data = await response.json();
    document.querySelector('#status').style.backgroundColor = '#009000';
    document.querySelector('#status').innerText = `닉네임 생성을 완료했습니다.`;
    document.querySelector('#name').innerText = data.name;
    document.querySelector('#description').innerText = data.description;
}