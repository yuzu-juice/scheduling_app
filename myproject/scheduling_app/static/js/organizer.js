document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth', // カレンダーの表示モードを指定
        selectable: true, // 日付を選択できるように設定
        unselectAuto: false, //カレンダー領域外をクリックしても選択解除しない
    });
    calendar.render();

    // 選択されている日付を管理する変数
    var selectedDate = null;

    // カレンダーの日付がクリックされたときの処理
    calendar.on('dateClick', function (info) {
        var clickedDate = info.dateStr;

        // 同じ日付を再度クリックした場合、選択を解除
        if (selectedDate === clickedDate) {
            selectedDate = null;
            calendar.unselect();
            document.getElementById('event-date').value = '';
        } else {
            // 異なる日付がクリックされた場合、選択を更新
            selectedDate = clickedDate;
            document.getElementById('event-date').value = selectedDate;
        }
    });
});
