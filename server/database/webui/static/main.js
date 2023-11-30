async function generateNickname() {
    const userPrompt = document.getElementById('user_prompt').value;
    if (!userPrompt.trim()) {
        document.querySelector('#user #status').innerText = '경고: 입력이 비어있습니다.';
        return;
    }
    document.querySelector('.chat #status').innerText = `잠시만 기다려주세요...`;
    const response = await fetch(`/api/generate?user_prompt=${userPrompt}`);
    const data = await response.json();
    document.querySelector('.chat #status').innerText = `닉네임 생성을 완료했습니다.`;
    document.querySelector('.chat #output.box').style.height = '10rem';
    document.querySelector('.chat #output.box').innerHTML = `<p>id:${data.uuid}</p><p>닉네임:${data.nickname}</p><p>설명:${data.explanation}</p>`;

}