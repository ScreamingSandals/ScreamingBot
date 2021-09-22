package org.screamingsandals.bot.misc;

import discord4j.core.DiscordClientBuilder;
import discord4j.core.GatewayDiscordClient;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;

import java.util.Objects;

@Slf4j
@Configuration
public class BeanConfig implements ApplicationContextAware {
    /**
     * <p>This is autowired by Spring.</p>
     */
    @Setter
    private ApplicationContext applicationContext;
    private Environment env;

    @Autowired
    public void setEnv(Environment env) {
        this.env = env;
    }

    @Bean
    public GatewayDiscordClient discordClient() {
        if (env.getProperty("bot.token") == null) {
            log.error("Discord bot token is null, can't continue.");
            ((ConfigurableApplicationContext) applicationContext).close();
            System.exit(1);
        }
        return DiscordClientBuilder.create(Objects.requireNonNull(this.env.getProperty("bot.token")))
                .build()
                .login()
                .block();
    }
}
