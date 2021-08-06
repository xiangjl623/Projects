package springboot.demo.ioc.config;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import springboot.demo.ioc.pojo.User;

public class IoCTest {
    public static void main(String[] args) {
        ApplicationContext ctx = new AnnotationConfigApplicationContext(AppConfig.class);
        User user = ctx.getBean(User.class);
        System.out.println(user.getId());
        System.out.println(user.getUserName());
        System.out.println(user.getNode());
    }
}
