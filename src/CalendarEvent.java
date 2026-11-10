
public class CalendarEvent {
    private String title;
    private int durationMinutes;

    public CalendarEvent(String title, int durationMinutes) {
        if (durationMinutes <= 0) {
            throw new IllegalArgumentException("Длительность должна быть больше 0");
        }
        this.title = title;
        this.durationMinutes = durationMinutes;
    }

    public static CalendarEvent fromHours(String title, double hours) {
        int minutes = (int) (hours * 60);
        return new CalendarEvent(title, minutes);
    }

    public static boolean isLong(int durationMinutes) {
        return durationMinutes >= 120;
    }

    public String getTitle() {
        return title;
    }

    public int getDurationMinutes() {
        return durationMinutes;
    }


    //работаем



    public static void main(String[] args) {
        CalendarEvent event1 = new CalendarEvent("Настил ковра", 120);
        System.out.println("Событие: " + event1.getTitle() + ", Длительность: " + event1.getDurationMinutes() + " мин.");

        CalendarEvent event2 = CalendarEvent.fromHours("Ларпить", 2.5);
        System.out.println("Событие: " + event2.getTitle() + ", Длительность: " + event2.getDurationMinutes() + " мин.");

        System.out.println(CalendarEvent.isLong(45));  
        System.out.println(CalendarEvent.isLong(150)); 
    }
}

