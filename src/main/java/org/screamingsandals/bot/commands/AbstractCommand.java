package org.screamingsandals.bot.commands;

import lombok.*;
import reactor.core.publisher.Mono;

import java.util.Arrays;
import java.util.List;
import java.util.function.Function;

@Getter
public abstract class AbstractCommand {
    private final String name;
    private final List<Argument<?>> args;

    public AbstractCommand(String name, Argument<?>... args) {
        this.name = name;
        this.args = Arrays.asList(args);
    }

    public abstract <T> Mono<Void> handle(List<ArgumentInstance<T>> args);

    @Data
    @Builder
    public static class Argument<T> {
        private Function<String, T> transformer;

        public ArgumentInstance<T> toInstance(String s) {
            return new ArgumentInstance<>(Argument.this, s);
        }
    }

    public record ArgumentInstance<T>(Argument<T> argument, String value) {
        T transform(String s) {
            return argument.transformer.apply(s);
        }
    }
}
