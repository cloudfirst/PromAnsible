describe("#Player", function() {

    beforeAll(function() {
        $(function () {
            $('#cronexp').jqCron({
                enabled_minute: false,
                multiple_dom: true,
                multiple_month: true,
                multiple_mins: false,
                multiple_dow: true,
                multiple_time_hours: true,
                multiple_time_minutes: false,
                default_period: 'week',
                default_value: '* * * * 1',
                no_reset_button: true,
                lang: 'en'
            });
        });
    });

    it("should translate every hour schedule correctly", function () {
        var cronExp = "43 * * * *";
        var cronHumanTextInEnglish = "Every hour at 43 minute(s) past the hour";

        $('#cronexp').jqCronGetInstance().setCron(cronExp);

        expect($('#cronexp').jqCronGetInstance().getHumanText()).toEqual(cronHumanTextInEnglish);
    });


    it("should translate every day schedule correctly", function () {
        var cronExp = "20 5,7,10 * * *";
        var cronHumanTextInEnglish = "Every day at 5,7,10:20";

        $('#cronexp').jqCronGetInstance().setCron(cronExp);

        expect($('#cronexp').jqCronGetInstance().getHumanText()).toEqual(cronHumanTextInEnglish);
    });

    it("should translate every week schedule correctly", function () {
        var cronExp = "20 10 * * 1-5";
        var cronHumanTextInEnglish = "Every week on monday-friday at 10:20";

        $('#cronexp').jqCronGetInstance().setCron(cronExp);

        expect($('#cronexp').jqCronGetInstance().getHumanText()).toEqual(cronHumanTextInEnglish);
    });

    it("should translate every month schedule correctly", function () {
        var cronExp = "52 8-9 26 * *";
        var cronHumanTextInEnglish = "Every month on 26 at 8-9:52";

        $('#cronexp').jqCronGetInstance().setCron(cronExp);

        expect($('#cronexp').jqCronGetInstance().getHumanText()).toEqual(cronHumanTextInEnglish);
    });

    it("should translate every year schedule correctly", function () {
        var cronExp = "34 21 3 5 *";
        var cronHumanTextInEnglish = "Every year on 3 of may at 21:34";

        $('#cronexp').jqCronGetInstance().setCron(cronExp);

        expect($('#cronexp').jqCronGetInstance().getHumanText()).toEqual(cronHumanTextInEnglish);
    });


});
