package org.screamingsandals.bot;

import discord4j.core.GatewayDiscordClient;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.ApplicationContext;

import java.util.Objects;

@SpringBootApplication
public class BotApplication {
	public static void main(String[] args) {
		ApplicationContext context = new SpringApplicationBuilder(BotApplication.class)
				.registerShutdownHook(true)
				.run(args);
		// halting the spring application to run indefinitely
		Objects.requireNonNull(context.getBean("discordClient", GatewayDiscordClient.class)).onDisconnect().block();
	}
}
