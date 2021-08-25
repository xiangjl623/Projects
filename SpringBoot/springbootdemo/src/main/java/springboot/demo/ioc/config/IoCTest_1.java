package springboot.demo.ioc.config;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import springboot.demo.ioc.config.User_1;

public class IoCTest_1 {
    public static void main(String[] args) {
        ApplicationContext ctx = new AnnotationConfigApplicationContext(AppConfig_1.class);
        User_1 user = ctx.getBean(User_1.class);
        System.out.println(user.getId());
        System.out.println(user.getUserName());
        System.out.println(user.getNote());
    }
}