package springboot.demo.ioc.pojo;

public class User {
    private Long id;
    private String userName;
    private String node;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getNode() {
        return node;
    }

    public void setNode(String node) {
        this.node = node;
    }
}
