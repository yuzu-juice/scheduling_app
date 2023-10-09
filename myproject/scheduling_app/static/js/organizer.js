document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth', // カレンダーの表示モードを指定
        unselectAuto: false, // カレンダー領域外をクリックしても選択解除しない
    });
    calendar.render();

    // 選択されている日付を管理する変数
    var selectedDates = [];

    // カレンダーの日付がクリックされたときの処理
    calendar.on('dateClick', function (info) {
        var clickedDate = info.dateStr;

        // すでに選択されている日付かどうかをチェック
        var index = selectedDates.indexOf(clickedDate);

        if (index === -1) {
            // 選択されていない場合、日付を選択リストに追加
            selectedDates.push(clickedDate);
            // カレンダーセルに色を付ける
            info.dayEl.style.backgroundColor = 'lightblue';
        } else {
            // すでに選択されている場合、日付を選択リストから削除
            selectedDates.splice(index, 1);
            // カレンダーセルの背景色を元に戻す
            info.dayEl.style.backgroundColor = '';
        }

        // フォームのhidden inputに選択された日付を設定
        document.getElementById('event-dates').value = selectedDates.join(',');
    });
});
