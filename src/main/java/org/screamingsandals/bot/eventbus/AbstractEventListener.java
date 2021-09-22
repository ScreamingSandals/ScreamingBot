package org.screamingsandals.bot.eventbus;

import discord4j.core.GatewayDiscordClient;
import discord4j.core.event.domain.Event;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.GenericTypeResolver;
import reactor.core.publisher.Mono;

import javax.annotation.PostConstruct;
import java.util.Objects;

public abstract class AbstractEventListener<T extends Event> {
    private GatewayDiscordClient client;

    @Autowired
    public final void setClient(GatewayDiscordClient client) {
        this.client = client;
    }

    @PostConstruct
    @SuppressWarnings("unchecked")
    public void construct() {
        client.on((Class<T>) Objects.requireNonNull(GenericTypeResolver.resolveTypeArgument(getClass(), AbstractEventListener.class)))
                .flatMap(this::handle)
                .subscribe();
    }

    protected abstract Mono<Void> handle(T event);
}
